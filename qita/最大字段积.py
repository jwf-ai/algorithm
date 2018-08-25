# encoding: utf-8

arr = [-1, -0.5, -3, -0.1, -1, -0.1, -9, -2]

res = arr[0]
max_m = arr[0]
min_m = arr[0]

for i in range(1,len(arr)):
    max_m = max(max_m * arr[i], min_m * arr[i], arr[i])
    min_m = min(max_m * arr[i], min_m * arr[i], arr[i])
    res = max(res,max_m)
print(res)