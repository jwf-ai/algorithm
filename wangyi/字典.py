#n,m,k = map(int,input().split())
# n = 2
# m = 2
# k = 6
#
# sstr = 'a'*n+'z'*m
# sstr = list(sstr)
# itr = 0
#
# def fun(sstr,start,end,k):
#
#     if start == end-1:
#         global itr
#         itr += 1
#         if itr == k:
#             print("".join(sstr))
#         return
#     for i in range(start,end):
#         if sstr[i] in sstr[start:i]:
#             continue
#         sstr[i],sstr[start] = sstr[start],sstr[i]
#         fun(sstr,start+1,end,k)
#         sstr[start],sstr[i] = sstr[i],sstr[start]
# fun(sstr,0,len(sstr),k)


n,m,k = map(int, input().split())

# 计算组合Cnm的大小，即是字母'a'和'z'的组合个数
def calc_comb(n,m):
    res = 1
    for i in range(1, n+m+1): #(n+1)!
        res *= i
    for j in range(1, n+1): # n!
        res //= j
    for k in range(1, m+1): # m!
        res //= k
    return res

if calc_comb(n, m) < k:
    print(-1)

else:
    k = k - 1
    res =""
    while n > 0 and m > 0:
        temp =calc_comb(n -1, m)
        if k < temp:
            res +='a'
            n -= 1
        else:
            res += 'z'
            m -= 1
            k = k - temp
    res +="a"*n
    res +="z"*m
    print(res)