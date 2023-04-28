s=''
ans = []
while True:
    if s == '.':
        break
    s = input()
    ans.append(s)
stack = []
ans = ans[0:len(ans)-1]
for i in ans:
    for j in range(len(i)):
        if i[j] == '(' or i[j] == '[':
            stack.append(i[j])
        elif  i[j] == ')':
            if len(stack)>0 and '(' == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(')')
                break
        elif i[j] == ']':
            if len(stack)>0 and'[' == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(']')
                break
    if len(stack)==0:
        print('yes')
    else:
        print('no')
    stack.clear()
