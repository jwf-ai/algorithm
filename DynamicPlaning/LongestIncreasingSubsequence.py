# encoding: utf-8

sequence = [1,7,3,5,9,4,8]


maxlen = [0] * len(sequence)
maxlen[0] = 1
s = []
s.append(sequence[0])
for i in range(1,len(sequence)):
    temp = 0
    ttt = -1
    for j in range(0,i):
        if sequence[i]>sequence[j]:
            if maxlen[j]>temp:
                temp = maxlen[j]
                ttt = j
    maxlen[i] = temp + 1
    if ttt != -1:
        s.append(ttt)


print(max(maxlen))
print(list(sequence[x] for x in s))