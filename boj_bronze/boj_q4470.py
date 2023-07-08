N = int(input())
words = []
for i in range(N):
    words.append(input())

index = 1
for i in words:
    answer = str(index) + "."
    print(answer, i)
    index += 1