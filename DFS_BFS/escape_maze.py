from collections import deque
n,m = map(int,input().split())
graph = []
for i in range(n):
    for j in range(m):
        graph.append(list(map(int,input())))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        queue.popleft()
