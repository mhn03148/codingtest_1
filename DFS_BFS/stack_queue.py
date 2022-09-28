from collections import deque
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])
#5
#52
#523
#5237
#523
#5231
#52314
#5231

queue = deque() #deque 라이브러리 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
#5
#25
#325
#7325
#732
#1732
#41732
#4173
