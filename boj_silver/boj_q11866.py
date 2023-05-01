N, K = map(int,input().split())
t = 0
arr=[]
ans = []
for i in range(N):
    arr.append(i+1)

while arr:
    for i in range(K-1):
        arr.append(arr.pop(0))
    ans.append(arr.pop(0))

s = str(ans)
s = s[1:]
s = s[:-1]
s = "<" + s + ">"
print(s)
