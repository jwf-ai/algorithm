# encoding: utf-8

# https://blog.csdn.net/zp_diandiandidi/article/details/63255143

def subset(arr,index,res):
    if index < len(arr):
        tmp = []
        for i in range(len(res)):
            t = res[i][:]
            t.append(arr[index])
            tmp.append(t)
        res.extend(tmp)
        subset(arr,index+1,res)

arr = [3,4,5]
index = 0
res = [[]]
subset(arr,index,res)
print(res)


def subset2(set,size):
    pow_set_size = pow(2,size)

    for i in range(pow_set_size):
        j = i
        k = 0
        print("{",end="")
        while j>0:
            if j & 1 == 1:
                print(set[k],end=" ")
            j >>=1
            k += 1
        print("}")

subset2(arr,len(arr))