# n,k = map(int,input().split())
# a = list(int(x) for x in input().split())

n = 3
k = 2
a = [5, 8, 5]

n, k = map(int, input().split())
a = list(int(x) for x in input().split())

rec = []

for i in range(k):
    if max(a) == min(a) or max(a) - min(a) == 1:
        break
    else:
        max_index = a.index(max(a))
        min_index = a.index(min(a))
        a[max_index] -= 1
        a[min_index] += 1
        rec.append((max_index + 1, min_index + 1))
s = max(a) - min(a)
m = len(rec)
print(s, m)
for r in rec:
    print(r[0], r[1])