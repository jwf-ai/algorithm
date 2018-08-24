# n = int(input())
# a = list(int(i) for i in input().split())
# m = int(input())
# q = list(int(i) for i in input().split())

n=5
a = [2, 7, 3, 4, 9]
m = 3
q = [1, 25, 11]

arr = [0]*(n+1)
for i in range(n):
    arr[i+1] = arr[i]+a[i]

def binarySearch(arr,key):
    left = 0
    right = len(arr)
    while(left <= right):
        mid = (left+right)//2
        if arr[mid-1]<key<=arr[mid]:
            return mid
        elif arr[mid]<key<arr[mid+1]:
            return mid + 1
        else:
            if arr[mid]>key:
                right = mid - 1
            else:
                left = mid + 1
    return -1

res = []
for qi in q:
    if qi<=arr[1]:
        print(1)
        continue
    else:
        index = binarySearch(arr,qi)
        print(index)
