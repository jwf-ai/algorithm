# encoding: utf-8

def largest_rectangle_area(arr):
    stack = []
    max_area = 0
    for i in range(len(arr)):

        while len(stack) !=0 and arr[i] <= arr[stack[-1]]:
            index = stack[-1]
            height = arr[index]
            stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            area = height * width
            if area > max_area:
                max_area = area

        stack.append(i)
    return max_area

arr = [2,1,5,6,2,3]
print(largest_rectangle_area(arr))