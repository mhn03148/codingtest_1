T = int(input())
ans=[]
for _ in range(T):
    a,b = map(int,input().split())
    ans.append([b,a])

ans.sort()
for i in range(len(ans)):
    print(ans[i][1], ans[i][0])