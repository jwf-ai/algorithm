# encoding: utf-8

def sum_num_least(arr,k):

    res = set()

    for i in range(len(arr)):
        j = i + 1
        t = len(arr) - 1
        while j < t:
            s = arr[i] + arr[j] + arr[t]
            if s <= k:
                tmp = [arr[i], arr[j], arr[t]]
                tmp.sort()
                res.add(tuple(tmp))
                j += 1
            else:
                t -= 1



    return res


def sum_num_equal(arr,k):

    res = set()

    for i in range(len(arr)):
        j = i + 1
        t = len(arr) - 1
        while j < t:
            s = arr[i] + arr[j] + arr[t]
            if s == k:
                tmp = [arr[i],arr[j],arr[t]]
                tmp.sort()
                res.add(tuple(tmp))
                t -= 1
                j += 1
            elif s > k:
                t -= 1
            else:
                j += 1


    return res



arr = [-1, 0, 1, 2, -1, 4]
print(sum_num_least(arr,0))