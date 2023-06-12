chess_board = []
for i in range(8):
    chess_board.append(input())

answer = 0

for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if chess_board[i][j] == 'F':
                    answer+=1
    else:
        for k in range(8):
            if k % 2 == 1:
                if chess_board[i][k] == 'F':
                    answer+=1

print(answer)