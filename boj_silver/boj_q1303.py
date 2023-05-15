N,M = map(int,input().split())
graph = []
for _ in range(M):
    graph.append(list(map(str,input())))
def dfs_W(x,y,z):
    if x <= -1 or x <= -1 or x>=M or y >=N:
        return False
    if graph[x][y] == "W":
        graph[x][y] = z
        dfs_W(x + 1,y,z)
        dfs_W(x, y + 1,z)
        dfs_W(x - 1, y,z)
        dfs_W(x, y - 1,z)
        return True

    return False
def dfs_B(x,y,z):
    if x <= -1 or x <= -1 or x>=M or y >=N:
        return False
    if graph[x][y] == "B":
        graph[x][y] = z
        dfs_B(x + 1,y,z)
        dfs_B(x, y + 1,z)
        dfs_B(x - 1, y,z)
        dfs_B(x, y - 1,z)
        return True
    else:
        return False

result = 0
result_1 = 0
num = 0
for i in range(M):
    for j in range(N):
        if dfs_W(i,j,num) == True:
            print(graph)
            result+=1
            num+=1
W_num = num
for i in range(M):
    for j in range(N):
        if dfs_B(i,j,num) == True:
            result_1+=1
            num+=1
ans = []
for i in range(num):
    ans_num=0
    for j in range(M):
        ans_num+=graph[j].count(i)
    ans.append(ans_num)

wPo=0
bPo=0
for i in range(len(ans)):
    if i < W_num:
        wPo += ans[i]**2
    else:
        bPo += ans[i]**2
print(graph)
print(wPo, bPo)
print(result, result_1)
