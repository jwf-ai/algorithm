# encoding: utf-8

def largest_rectangle_area(A):
    n = len(A)

    stack = []
    max_area = 0
    i = 0
    while i < n:
        if len(stack) == 0 or A[i] >= A[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            index = stack.pop()
            height = A[index]
            width = i - stack[-1] - 1 if len(stack) != 0 else i
            area = height * width
            max_area = max(max_area, area)
    while stack:
        index = stack.pop()
        height = A[index]
        width = i - stack[-1] - 1 if len(stack) != 0 else i
        area = height * width
        max_area = max(max_area, area)

    return max_area

arr = [2,1,5,6,2,3]
print(largest_rectangle_area(arr))