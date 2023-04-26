from collections import deque
n, m = map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0,0))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y]+1
            q.append((nx,ny))
print(maze[n-1][m-1])