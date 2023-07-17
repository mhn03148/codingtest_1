P, k = map(int, input().split())

answer = 0
for i in range(2,P):
    if i >= k:
        print("GOOD")
        break
    else:
        if P % i == 0:
            answer = i
            print("BAD", answer)
            break

