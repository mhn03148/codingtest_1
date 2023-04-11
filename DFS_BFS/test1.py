square = [[0,0,1],[0,0,0],[1,1,1]]
answer = [[]]
test = []
for i in range(len(square)*2):

    if i < (len(square)):

        for j in range(len(square)*2):
            if i < len(square) and j < len(square):
                test.append(square[i][j])
            elif i < len(square) and j >len(square)-1:
                test.append(square[i][len(square)*2-j-1])
        print(i)
        print()
    else:
        print(i)
        print(answer[len(square)*2-i-1])
        answer.append(answer[len(square)*2-i-1])
    #print(test[i*len(square)*2:(i+1)*len(square)*2])
    answer.insert(i,test[i*len(square)*2:(i+1)*len(square)*2])
    test1 = [[] for i in range(5)]
    for i in range(5):
        for j in range(5):
            test1[i].append(j)
print(test)
print(test1)
print(answer)