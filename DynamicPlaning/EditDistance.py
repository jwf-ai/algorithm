# encoding: utf-8

S = input()
T = input()

def fun(str1,str2):
    A = list([0]*(len(str2)+1) for i in range(len(str1)+1))
    for i in range(len(str1)+1):
        A[i][0] = i
    for j in range(len(str2)+1):
        A[0][j] = j
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i - 1] != str2[j - 1]:
                A[i][j] = min(A[i - 1][j] + 1, A[i][j - 1] + 1, A[i - 1][j - 1] + 1)
            else:
                A[i][j] = min(A[i - 1][j] + 1, A[i][j - 1] + 1, A[i - 1][j - 1])
    return A[len(str1)][len(str2)]

print(fun(S,T))