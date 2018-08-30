# encoding: utf-8
from itertools import combinations,permutations

def combination1(arr,r):
    return list(combinations(arr,r))

def permutation1(arr,r):
    return list(permutations(arr,r))

def combination2(arr,r):
    # 递归法
    def recursion(res,arr,n,m,b,r):
        if m == 0:
            res.append(b[:])
            return
        for i in range(n,m-1,-1):
            b[m-1] = arr[i-1]
            recursion(res,arr,i-1,m-1,b,r)
    res = []
    b = [0] * r
    recursion(res,arr,len(arr),r,b,r)
    return res


def permutation2(arr, r):
    # 递归法
    def recursion(res, arr, start, end):
        if start == end:
            res.append(arr[:])
            return
        for i in range(start,end,1):
            if arr[i] in arr[start:i]:
                continue
            arr[start],arr[i] = arr[i],arr[start]
            recursion(res,arr,start+1,end)
            arr[start],arr[i] = arr[i],arr[start]

    res = []
    per = combination2(arr,r)
    for p in per:
        tmp = []
        recursion(tmp, p, 0, len(p))
        res.extend(tmp)
    return res

if __name__ == "__main__":

    arr = [1,2,4,4]
    print(combination1(arr,2))
    print(combination2(arr,2))

    print(permutation1(arr,4))
    print(permutation2(arr,4))