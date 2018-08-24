n,k = map(int,input().split())
a = list(int(i) for i in input().split())
t = list(int(i) for i in input().split())

sum_i = 0
sum_j = 0

for i in range(k):
    if t[i] == 0:
        sum_j += a[i]
    else:
        sum_i += a[i]
last_temp = sum_j
for i in range(k,len(t)):
    temp = last_temp
    if t[i] == 1:
        sum_i += a[i]
    else:
        temp += a[i]
    if t[i-k] == 0:
        temp -= a[i-k]
    if temp>sum_j:
        sum_j = temp
    last_temp = temp
print(sum_i+sum_j)