from collections import deque
n ,m, v = map(int,input().split())
q = []
graph = [[]]
graph2 = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited_b = [False] * (n+1)
for i in range(1,n+1):
    graph.append(list(map(int,input().split())))

for i in range(1,n+1):
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
