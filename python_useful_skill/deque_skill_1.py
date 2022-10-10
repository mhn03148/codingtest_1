from collections import deque


#q = deque(s)
'''
j = len(q)
while q:
    before_q=len(q)
    for i in range(len(q)-1):
        if q[i]!=q[i+1]:
            continue
        if q[i] == q[i+1]:
            q.popleft()
            q.popleft()
            j -= 2
            break
    if before_q == len(q):
        break
    if len(q)==0:
        print (q)
        break
    print(q)
    j -= 1
'''
def solution(s):
    stack = []
    #stack.append(s[0])
    j=0
    for i in range(0,len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[j] != s[i]:
                stack.append(s[i])
                j+=1
            elif stack[j] == s[i]:
                stack.pop()
                j-=1
                if len(stack) == 0:
                    j = 0
        print(stack)
        print(j)
    if len(stack) == 0:
        return 1
    else:
        return 0

s = "baabaa"
print(solution(s))
