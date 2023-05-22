A,B = map(int,input().split())
ans = []
ans.append(0)
for i in range(1000):
    for j in range(i):
        ans.append(i)

res = 0
for i in range(A,B+1):
    result= ans[i] + result

print(res)