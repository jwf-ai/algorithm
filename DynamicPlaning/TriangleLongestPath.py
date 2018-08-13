# encoding: utf-8

data = [
    [7],
    [3,8],
    [8,1,0],
    [2,7,4,4],
    [4,5,2,6,5]
]

n = 5

def longestPath(i,j):
    if i == n:
        return 0
    x = longestPath(i+1,j)
    y = longestPath(i+1,j+1)
    if x < y:
        x = y
    return x + data[i][j]

print(longestPath(0,0))
