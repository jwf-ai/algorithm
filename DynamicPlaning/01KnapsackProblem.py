# encoding: utf-8


########input#########
"""
5 10
2 6
2 3
6 5
5 4
4 6
"""
n,C = map(int,input().split())

d = list(list(int(x) for x in input().split()) for i in range(n))
w = list(i[0] for i in d)
v = list(i[1] for i in d)

maxValue = [[0]*(C+1) for i in range(n)]

for i in range(n):
    for j in range(C+1):
        if i == 0:
            if j>=w[i]:
                maxValue[i][j] = v[i]
            else:
                maxValue[i][j] = 0
        else:
            if j >= w[i]:
                maxValue[i][j] = max(maxValue[i-1][j],maxValue[i-1][j-w[i]]+v[i])
            else:
                maxValue[i][j] = maxValue[i-1][j]

print(maxValue[n-1][C])


