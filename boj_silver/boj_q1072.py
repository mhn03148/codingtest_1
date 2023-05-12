X, Y = map(int,input().split())
Z = (Y*100)//X
st = 1
en = 1000000000
while st<=en:
    mid = (st+en)//2
    if Z <((Y + mid)*100 //(X + mid)):
        en = mid-1
    else:
        st = mid+1

if st > 1000000000:
    print(-1)
else:
    print(st)