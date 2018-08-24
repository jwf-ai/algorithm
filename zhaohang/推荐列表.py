m,n = map(int,input().split())
P = list(list(x for x in input().split() if x!='*') for i in range(m))

if n == 0:
    Z = set()
    for p in P:
        Z.update(p)
    if len(Z) == 0:
        print("None")
    else:
        print(" ".join(Z))
else:

    Q = {}
    for p in P:
        if p[0] in Q.keys():
            Q[p[0]].update(p[1:])
        else:
            Q[p[0]] = set(p[1:])
        for key in Q.keys():
            if p[0] in Q[key]:
                Q[p[0]].update(p[1:])
    res = []
    if len(res) == 0:
        print("None")
    for key in Q.keys():
        if len(Q[key])>=n:
            res.append(key)
    print(" ".join(res))

"""
5 0
A B C
C F *
B D E
D G *
E H I
"""