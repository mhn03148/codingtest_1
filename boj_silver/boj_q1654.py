K, N = map(int,input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))

st = 1
en = max(lan)
while st<en:
    cur = 0
    mid = (st + en + 1)//2
    for i in lan:
        cur += i//mid
    if cur < N:
        en = mid-1
    else:
        st = mid

print(st)