T = int(input())
time = list(map(int,input().split()))
time.sort()
ans = 0
ansList = []
for i in time:
    ans = ans + i
    ansList.append(ans)

print(sum(ansList))