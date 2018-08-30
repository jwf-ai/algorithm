# encoding: utf-8

"""
给你一个只由0和1组成的矩阵，找出一个最大的子矩阵，要求这个子矩阵是方阵，并且这个子矩阵的所有元素为1
"""

def max_square_mat(mat):
    row = len(mat)
    col = len(mat[0])

    if row == 0:
        return

    mat_len = 0
    if row < col:
        mat_len = row
    else:
        mat_len = col


    for k in range(mat_len,0,-1):

        for i in range(row - k +1):
            for j in range(col - k + 1):
                res = []
                flag = True
                for t in range(k):
                    res.append(mat[i+t][j:j+k])
                    if sum(mat[i+t][j:j+k]) != k:
                        flag = False
                        break
                if flag == True:
                    return res

    return

def max_square_mat_2(mat):
    m = len(mat)
    n = len(mat[0])
    max = -1
    for i in range(1,m):
        for j in range(1,n):
            if mat[i][j] == 1:
                mat[i][j] += min(mat[i-1][j-1],mat[i-1][j],mat[i][j-1])
                if max < mat[i][j]:
                    max = mat[i][j]
    return max

mat = [
    [0,1,1,1],
    [1,1,1,0],
    [0,1,1,1]
]

print(max_square_mat(mat))
print(max_square_mat_2(mat))
