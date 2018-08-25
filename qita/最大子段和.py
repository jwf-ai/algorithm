# encoding: utf-8

arr = [-1, -2, -3, -10, -4, -7, -2, -5]

result = arr[0]
sum = arr[0]

for i in range(1,len(arr)):
  sum = max(sum+arr[i],arr[i])
  result = max(result,sum)

print(result)

