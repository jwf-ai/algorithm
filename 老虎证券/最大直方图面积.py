# encoding: utf-8

histogram = [2,7,9,4,1]

def max_rectangle_area(histogram):

    stack = []
    max_area = 0

    for i in range(len(histogram)):
        if len(stack) == 0 or histogram[i] >= histogram[stack[-1]]:
            stack.append(i)
        else:
            while len(stack) != 0 and histogram[stack[-1]] >= histogram[i]:
                last_index = stack.pop()
                left_index = stack[-1] if len(stack) > 0 else 0
                area = histogram[last_index] * (i - left_index-1)
                max_area = max(max_area,area)
            stack.append(i)
    return max_area

print(max_rectangle_area(histogram))


