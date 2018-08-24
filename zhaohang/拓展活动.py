#k,n = map(int,input().split())
k = 3
n = 15

def f(arr,i,k,n):
    if n<0 or len(arr)>k:
        return
    if len(arr) == k and n == 0:
        print(" ".join(list(str(x) for x in arr)))
        return

    for j in range(i+1, 10):
        temp = arr.copy()
        temp.append(j)
        f(temp, j, k, n - j)

f([],0,k,n)