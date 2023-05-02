a, b, c =1,1,1
ans = []
while a!=0:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        continue
    else:
        ans.append([a,b,c])

def triangle(ans):
    ans.sort()
    if ans[2]**2 == ans[1]**2 + ans[0]**2:
        return("right")
    else:
        return("wrong")
    print(ans)
    return(ans)

for i in ans:
    print(triangle(i))


