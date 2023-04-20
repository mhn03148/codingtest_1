ans = []
while True:
    A, B = map(int,input().split())
    if A>B:
        ans.append('Yes')
    elif A==0 and B==0:
        break
    else:
        ans.append('No')

for i in ans:
    print(i,end='\n')