import sys
sys.setrecursionlimit(10**6)
#파이썬이 정한 최대 recursion을 임의로 설정해주는 방법
def dfs(x, y, map):
    if x <= -1 or y <= -1 or x >= len(map) or y >= len(map[0]):
        return False

    if map[x][y] == 1:
        map[x][y] = 0
        dfs(x + 1, y, map)
        dfs(x, y + 1, map)
        dfs(x - 1, y, map)
        dfs(x, y - 1, map)
        return True
    return False

ans = []
T = int(input())
bae_graph = []
for i in range(T):
    a, b, c = map(int,input().split())
    graph = [[0]*a for _ in range(b)]
    for j in range(c):
        y, x = map(int,input().split())
        graph[x][y] = 1
    result = 0
    for k in range(a):
        for l in range(b):
            if dfs(l,k,graph) == True:
                result+=1
    ans.append(result)
for i in ans:
    print(i, end="\n")