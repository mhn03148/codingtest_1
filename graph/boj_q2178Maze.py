from collections import deque
N,M = map(int,input().split())
maze = [[0] * M for _ in range(N)]
distance = 0

for i in range(N):
    s = input()
    for j in range(M):
        maze[i][j]=(int(s[j]))

print(maze)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

q = deque()
q.append((0,0))
print(maze[0][0])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < N and 0<= ny < M  and maze[nx][ny] == 1:
            print(nx,ny)
            q.append((nx,ny))
            print(q)
            maze[nx][ny]=maze[x][y]+1


print(maze)
print(maze[N-1][M-1])