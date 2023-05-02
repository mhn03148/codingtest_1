s = ''
ans = []
while s !='0':
    s = input()
    if s == s[::-1]:
        ans.append('yes')
    else:
        ans.append('no')
for i in range(len(ans)-1):
    print(ans[i],end='\n')