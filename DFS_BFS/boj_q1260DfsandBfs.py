
from collections import deque
n ,m, v = map(int,input().split())
q = []
graph = [[]]
graph2 = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited_b = [False] * (n+1)
for i in range(1,m+1):
    graph.append(list(map(int,input().split())))

for i in range(1,m+1):
    graph2[graph[i][0]].append(graph[i][1])
    graph2[graph[i][1]].append(graph[i][0])


def dfs(graph2,v,visited):
    visited[v] = True
    print(v, end=' ')
    graph2[v].sort()
    for i in graph2[v]:
        if not visited[i]:
            dfs(graph2,i,visited)


def bfs(graph2,v,visited_b):
    queue = deque([v])
    visited_b[v] = True
    while queue:
        k = queue.popleft()
        print(k, end=' ')
        graph2[k].sort()
        for i in graph2[k]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True

dfs(graph2,v,visited)
print(end="\n")
bfs(graph2,v,visited_b)
'''
def DFS(v):
    visited[v]=1
    dfs.append(v)
    for i in node[v]:
        if (visited[i]==0):
            DFS(i)

def BFS(v):
    visited[v]=1
    bfs.append(v)
    queue = [v]

    while(queue):
        for i in node[queue.pop(0)]:
            if(visited[i]==0):
                visited[i]=1
                bfs.append(i)
                queue.append(i)
##################MAIN##################
N, M, V = map(int, input().split())

node =[[]for _ in range(N+1)]
visited = [0]*(N+1)
dfs = []
bfs = []

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N+1):
    node[j].sort()

DFS(V)
for j in range(N+1):
    visited[j]=0
BFS(V)

for m in dfs:
    print(m, end=' ')
print()
for n in bfs:
    print(n, end=' ')
'''