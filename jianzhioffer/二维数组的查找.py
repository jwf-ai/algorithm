
def Find(target, array):
    # write code here
    rows = len(array) - 1
    cols= len(array[0]) - 1
    i = rows
    j = 0
    while j<=cols and i>=0:
        if target<array[i][j]:
            i -= 1
        elif target>array[i][j]:
            j += 1
        else:
            return True
    return False

if __name__ == "__main__":
    array = [
        [1, 2, 3,  4,  5,  6],
        [2, 3, 4,  5,  7,  9],
        [3, 5, 6, 10, 13, 18],
        [4, 6, 8, 13, 14, 19]
    ]

    res = Find(8,array)
    print(res)