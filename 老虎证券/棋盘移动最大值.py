A = [
    [2,3,4,7],
    [1,4,6,7],
    [1,5,7,2],
    [50,4,1,7]
]

max_sum = list([0] * len(A[0]) for i in range(len(A)))
max_sum[0][0] = 2

def run(A,max_sum):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0 :
                max_sum[i][j] = max_sum[i][j-1]+A[i][j]
            elif j == 0:
                max_sum[i][j] = max_sum[i-1][j] + A[i][j]
            else:
                max_sum[i][j] = max(max_sum[i-1][j] + A[i][j],max_sum[i][j-1]+A[i][j])

    return max_sum[len(A)-1][len(A[0])-1]


print(run(A,max_sum))