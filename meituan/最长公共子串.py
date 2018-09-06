# encoding: utf-8

A = "abcde"
B = "ebgde"

def longest_common_substring(A, B):
    m = len(A)
    n = len(B)
    if m == 0 or n == 0:
        return 0
    mat = list([0] * n for i in range(m))
    max_length = 0
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                if i == 0 or j == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i-1][j-1] + 1
                max_length = max(max_length,mat[i][j])
    return max_length
print(longest_common_substring(A,B))