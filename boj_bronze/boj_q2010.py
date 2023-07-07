N = int(input())
answer = 0
for i in range(N):
    answer += int(input())

print(answer - (N-1))