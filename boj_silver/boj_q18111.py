import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
ans = sys.maxsize
mymap = []
tar = 0
for i in range(N):
    mymap.append(list(map(int,input().split())))
for level in range(257):
    Max, Min = 0, 0
    for i in range(N):
        for j in range(M):
            if mymap[i][j] >= level:
                Max += mymap[i][j] - level
            else:
                Min += level-mymap[i][j]
    if Max + B >= Min:
        if Min + (Max*2) <= ans:
            ans = Min + (Max*2)
            tar = level

print(ans,tar)

