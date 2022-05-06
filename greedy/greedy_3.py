N, K = map(int,input().split())

ans = 0
while N >= K:
    if (N % K == 0):
        N = N//K
        ans +=1
    else:
        N = N-1
        ans +=1

print(N)
while N > 1:
    N = N-1
    ans += 1



print(ans)