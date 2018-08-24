n,m = map(int, input().split())
C = list(int(i) for i in input().split())

Z = list([] for i in range(n))

for ci in C:
    Z[ci-1].append(1)

l = (len(i) for i in Z)
print(min(l))