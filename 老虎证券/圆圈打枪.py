# encoding: utf-8

# 有循环
A = list(i for i in range(1,1001,1))
dead = False
while True:
    tmp = A.pop(0)
    if len(A) == 0:
        if dead == False:
            print(tmp)
        else:
            print(A[0])
        break
    if dead == False:
        A.append(tmp)
        dead = True
    else:
        dead = False

# 无循环
A = list(i for i in range(501))
while len(A)!=1:
    tmp = []
    for i in range(len(A)):
        if i % 2 == 1:
            tmp.append(A[i])
    A = tmp
print(A)