def Solve(N,M,map,res):
    a=M/2
    b=M-a*2

    E=list([100000000] * N for i in range(N))

    if a==1:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i!=k and j!=k and res[i][j]>map[i][k]+map[k][j]:
                        res[i][j]=map[i][k]+map[k][j]
        if 1==b:
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        if j!=k and E[i][j]>res[i][k]+map[k][j]:
                            E[i][j]=map[k][j]+res[i][k]
            for i in range(N):
                for j in range(N):
                    res[i][j]=E[i][j]

        return

    Solve(N,a,map,res)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if E[i][j]>res[i][k]+res[k][j]:
                    E[i][j]=res[i][k]+res[k][j]

    E = list([100000000] * N for i in range(N))


    if b==1:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if j!=k and E[i][j]>res[i][k]+map[k][j]:
                        E[i][j]=res[i][k]+map[k][j]
        for i in range(N):
            for j in range(N):
                res[i][j] = E[i][j]


if __name__ == "__main__":
    N,M = map(int,input().split())

    map = list(list(int(x) for x in input().split()) for i in range(N))

    res = list([100000000] * N for i in range(N))
    Solve(N,M,map,res)
    for i in range(N):
        print(" ".join(str(res[i])))

    """
    3 2
    0 2 3
    2 0 1
    3 1 0
    """