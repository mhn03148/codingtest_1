N = int(input())
playerName = []
playerFirstLatter = []
answer = []
Answer = "PREDAJA"
for _ in range(N):
    name = input()
    playerName.append(name)
    playerFirstLatter.append(name[0])

for i in playerName:
    if playerFirstLatter.count(i[0]) >= 5:
        answer.append(i[0])

if len(answer) > 0:
    Answer = ""
    answer = list (set(answer))
    answer.sort()
    for i in answer:
        Answer += i

print(Answer)

