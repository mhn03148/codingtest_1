N, K= map(int, input().split())
coin = []
ans = 0
for i in range(N):
    coin.append(int(input()))

coin = coin[::-1]

while K>0:
    for i in range(len(coin)):
        if K >= coin[i]:
            ans = ans + K // coin[i]
            K = K % coin[i]
        else:
            continue

print(ans)