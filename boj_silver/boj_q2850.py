N, M = map(int,input().split())
tree = list(map(int,input().split()))
st = 1
en = max(tree)

while(st<en):
    cur = 0
    mid = (st + en+1)//2
    for i in tree:
        if i > mid:
            cur+= i-mid
    if cur < M:
        en = mid-1
    else:
        st = mid
print(st)
