# encoding: utf-8

Arr = "89 9399 9143"

Arr_L = Arr.split(' ')
N = len(Arr_L)

maxL = 0
for i in range(N):
    if len(Arr_L[i])>maxL:
        maxL = len(Arr_L[i])
    temp = int(Arr_L[i])
    restr = Arr_L[i]
    restr = list(restr)
    restr.reverse()
    restr = "".join(restr)

    re = int(restr)
    if re > temp:
        Arr_L[i] = restr

print(Arr_L)

Array = Arr_L.copy()
for i in range(N):
    Array[i] = Arr_L[i] + "0"*(maxL-len(Arr_L[i]))

print(Arr_L)



Ans = ''
while len(Array) != 0:
    max_i = Array.index(max(Array))
    Ans = Ans+Arr_L[max_i]
    Array.pop(max_i)
    Arr_L.pop(max_i)
print(Ans)
