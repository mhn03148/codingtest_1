T = int(input())
p = []
ans = []
ans_1 = []
n = 1
for i in range(T):
    p.append(int(input()))

while p:
    if T+1<n:
        ans.append('NO')
        break
    if len(ans_1)>0 and p[0] == ans_1[-1]:
        p.pop(0)
        ans_1.pop(-1)
        ans.append('-')
    elif len(ans_1)==0 or p[0] != ans_1[-1]:
        ans_1.append(n)
        ans.append("+")
        n += 1

if 'NO' in ans:
    print('NO')
else:
    for i in ans:
        print(i, end='\n')