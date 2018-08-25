# encoding: utf-8



def max_subsequence(arr):

    if len(arr) < 2:
        return

    a = [] # num(0)-num(1)
    b = [-1] * (2*len(arr)+1)
    if arr[0] == 0:
        a.append(1)
        b[1] = 0
    else:
        a.append(-1)
        b[-1] = 0
    res = []
    for i in range(1,len(arr)):
        if arr[i] == 0:
            diff = a[i-1] + 1
            a.append(diff)
        else:
            diff = a[-1] - 1
            a.append(diff)

        last_index = b[diff]
        if last_index != -1:
            if i - last_index > len(res):
                res = arr[last_index+1:i+1]
        else:
            b[diff] = i

    return res


arr = [0,0,0,0,1,0,0,1,1,0,1,1,0,0]
print(max_subsequence(arr))

