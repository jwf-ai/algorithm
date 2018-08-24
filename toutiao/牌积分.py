# encoding: utf-8

scores = [
    (9,7),
    (5,3),
    (5,8),
    (3,7),
    (1,4),
    (8,5),
    (4,2),
    (1,3)]

scores = sorted(scores,key = lambda i:[i[0]],reverse=True)
print(scores)

a = 0
b = 0
sum_score = 0
temp = 0
for i in range(0,len(scores)):
    if a > b:
        b += scores[i][0]
        temp += scores[i][1]
    elif a < b:
        a += scores[i][0]
        temp += scores[i][1]
    else:
        if temp > sum_score:
            sum_score = temp
        a += scores[i][0]
        temp += scores[i][1]
    if a == b:
        if temp > sum_score:
            sum_score = temp

if sum_score == 0:
    print("None")
else:
    print(sum_score)