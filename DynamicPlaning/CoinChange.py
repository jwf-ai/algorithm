# encoding: utf-8

N = int(input())
minCount = [0]*(N+1)

for i in range(1,N+1):
    a = N+1
    b = N+1
    c = N+1

    if i >= 1:
        a = minCount[i-1] + 1
    if i >= 3:
        b = minCount[i-3] + 1
    if i >= 5:
        c = minCount[i-5] + 1

    d = min([a,b,c])
    minCount[i] = d

print(minCount[N])