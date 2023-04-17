import heapq
num = int(input())
card = []
result = 0
for i in range(num):
    heapq.heappush(card,(int(input())))
card.sort()

if len(card)==0:
    print(0)
else:
    while(len(card)>1):
        plus = heapq.heappop(card) + heapq.heappop(card)
        result += plus
        heapq.heappush(card,plus)

    print(result)

