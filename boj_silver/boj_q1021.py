from collections import deque
N, M = map(int,input().split(" "))

numberArray = []
for i in range(1,N+1):
    numberArray.append(i)

dequeArray = deque(numberArray)
findNumberArray = list(map(int,input().split(" ")))

count = 0

for i in findNumberArray:
    if dequeArray.index(i) < (len(dequeArray))-dequeArray.index(i):
        for _ in range(dequeArray.index(i)):
            dequeArray.append(dequeArray.popleft())
            count += 1
    else:
        for _ in range((len(dequeArray))-dequeArray.index(i)):
            dequeArray.appendleft(dequeArray.pop())
            count += 1
    dequeArray.popleft()

print(count)