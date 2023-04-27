from collections import deque
T = int(input())
ans = []
answer = []
q = deque()
for i in range(T):
    ans.append(input().split())

for i in ans:
    if i[0] == 'push':
        q.append(i[1])
    elif i[0] == 'pop':
        if len(q) == 0:
            answer.append(-1)
        else:
            answer.append(q.pop())
    elif i[0] == 'size':
        answer.append(len(q))
    elif i[0] == 'empty':
        if len(q) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif i[0] == 'top':
        if len(q) == 0:
            answer.append(-1)
        else:
            answer.append(q[-1])


for i in answer:
    print(i, end="\n")