N, K= map(int, input().split())
coin = []
ans = 0
for i in range(N):
    coin.append(int(input()))

coin = coin[::-1]
coin.append(0)
while K>0:
    for i in range(len(coin)):
        if coin[i] > K > coin[i + 1]:
            ans = ans + K //coin[i+1]
            K = K % coin[i+1]

print(ans)