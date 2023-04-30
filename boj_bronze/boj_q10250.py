T = int(input())
ans = []
for i in range(T):
    H, W, N =map(int,input().split())
    a = N // H + 1
    b = N % H
    if b == 0:
        b = H
        a = N//H
    if a < 10:
        s =str(b)+'0'+str(a)
    else:
        s = str(b) + str(a)
    ans.append(s)

for i in ans:
    print(i, end='\n')