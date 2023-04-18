co = list(map(int,input().split()))
ans = [co[0],co[1],co[2]-co[0],co[3]-co[1]]
print(min(ans))