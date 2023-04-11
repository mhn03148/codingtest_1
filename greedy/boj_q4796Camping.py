List=[1]
numList = []
while sum(List) !=0:
    List = list(map(int,input().split()))
    if sum(List)>0:
        numList.append(List)

for i in range(len(numList)):
    # 총 휴가 일수를 연속하는 날짜로 나눈 수가 연속으로 사용하는 수보다 크면 나머지 수를 더하는게 아닌 연속으로 가능한 수를 더해줘야 한다.
    if numList[i][0] < numList[i][2] % numList[i][1]:
        print("Case {0}:".format(i + 1),
              (numList[i][2] // numList[i][1]) * numList[i][0] + numList[i][0])
    else:
        print("Case {0}:".format(i+1), (numList[i][2] // numList[i][1]) * numList[i][0] + (numList[i][2] % numList[i][1]))

