n,m = map(int,input().split())

board=[]
count=[]
for i in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):
        W = 0
        B = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if board[i][j]!= 'W':
                        W += 1
                    else:
                        B += 1
                else:
                    if board[i][j]!= 'W':
                        B += 1
                    else:
                        W += 1
        count.append(B)
        count.append(W)

print(min(count))