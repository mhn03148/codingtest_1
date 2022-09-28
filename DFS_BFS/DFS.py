def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:#visited[i]가 False일 경우
            dfs(graph, i , visited)

graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]
visited = [False] * 9

dfs(graph,1,visited)

#list에 Fasle가 있을때, if not list[]: 면 동작
list1 = [False,False,True]
print(list1)
for i in range(3):
    if not list1[i]:
        print('hello')

