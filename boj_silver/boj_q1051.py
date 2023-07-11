N , M = map(int, input().split())
square = []
answer = []
for i in range(N):
    square.append(list(map(int,input())))

for a in range(1, min(N,M)):
    for i in range(N-a):
        for j in range(M-a):
            if square[i][j] == square[i+a][j] and square[i+a][j] == square[i][j+a] and square[i][j+a] == square[i+a][j+a]:
                answer.append(a+1)


if len(answer) == 0:
    print(1)
else:
    print(max(answer)**2)

