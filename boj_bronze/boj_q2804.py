A, B = map(str,input().split(" "))
cross = []
crossword = [["." for i in range(len(A))] for j in range(len(B))]

for i in range(len(A)):
    if A[i] in B:
        cross.append([i,B.index(A[i])])
        break


for i in range(len(B)):
    for j in range(len(A)):
        if i == cross[0][1]:
            crossword[i][j] = A[j]
        if j == cross[0][0]:
            crossword[i][j] = B[i]


for word in crossword:
    for i in word:
        print(i, end="")
    print(end="\n")