# encoding: utf-8


n = int(input())

v = [1, 5, 10, 20, 50, 100]
k = len(v)


def num_of_combinations(n, k, v):
    if n == 0:
        return 1
    elif n < 0 or k <= 0:
        return 0
    else:
        return num_of_combinations(n,k-1,v) + num_of_combinations(n-v[k-1],k,v)

print(num_of_combinations(n,k,v))

def num_of_combinations1(n, k, v):

    tc = list([0] * (n+1) for i in range(k))
    # 只用1进行找零，所以方案全为0
    for i in range(n+1):
        tc[0][i] = 1

    # tc[i][j] = tc[i-1][j] + t[i][j-v[i]]
    for i in range(1,k):
        for j in range(n+1):
            if j - v[i] < 0:
                temp = 0
            else:
                #print(k,i)
                #print(n+1,j - v[i])
                temp = tc[i][j - v[i]]

            tc[i][j] = tc[i - 1][j] + temp#tc[i][j - v[i]]

    return tc[k-1][n]

print(num_of_combinations1(n,k,v))






