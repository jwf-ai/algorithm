# encoding: utf-8

S = input()
T = input()

S = " "+S
T = " "+T

m = list([0] * (len(T)) for i in range((len(S))))
print(len(m),len(m[0]))

for i in range(len(S)):
    for j in range(len(T)):
        if i == 0:
            print(i, j)
            m[i][j] = j
            continue
        if j == 0:
            m[i][j] = i
            continue
        if S[i] == T[j]:
            m[i][j] = m[i-1][j-1]
        else:
            modify = m[i-1][j-1]+1
            insertOrDelete = min(m[i-1][j-1]+1,m[i][j-1]+1)
            m[i][j] = min(modify,insertOrDelete)

print(m[len(S)-1][len(T)-1])
