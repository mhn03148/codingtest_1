K = int(input())
ans = []
for _ in range(K):
    i = int(input())
    if i == 0:
        ans.pop(-1)
    else:
        ans.append(i)
print(sum(ans))