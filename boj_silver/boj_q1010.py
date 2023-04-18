import math
c = int(input())
ans = []
for i in range(c):
    N,M = map(int,input().split())
    ans.append(math.factorial(M) / (math.factorial(N) * math.factorial(M-N)))

for i in ans:
    print(int(i),end="\n")