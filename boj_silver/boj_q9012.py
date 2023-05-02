T = int(input())
s = []
stack = []
for i in range(T):
    s.append(input())

for i in s:
    stack.clear()
    for j in range(len(i)):
        if i[j] == '(':
            stack.append(i[j])
        elif i[j] == ')' and len(stack)>0:
            if stack[-1] == "(":
                stack.pop(-1)
        else:
            stack.append(i[j])
    if len(stack)>0:
        print("NO")
    else:
        print('YES')
