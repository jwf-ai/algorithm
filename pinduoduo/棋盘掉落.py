# encoding: utf-8

def drop(chessboard):
    for j in range(len(chessboard[0])):
        for i in range(len(chessboard)-1,-1,-1):
            if chessboard[i][j] == 'o':
                if i == len(chessboard) - 1:
                    chessboard[i][j] = '.'
                else:
                    temp = i
                    while temp<=len(chessboard)-2:
                        if chessboard[temp+1][j] == '.':
                            chessboard[temp][j] = '.'
                            chessboard[temp+1][j] = 'o'
                        else:
                            break
                        temp += 1
                    if temp == len(chessboard)-1 and chessboard[temp][j] == 'o':
                        chessboard[temp][j] = '.'

    for row in chessboard:
        print(row)




chessboard = [
    ['.','o','o','o','o','x'],
    ['.','.','x','o','o','o'],
    ['.','o','o','.','x','.'],
    ['.','.','.','x','o','x']
]

drop(chessboard)