'''''
예제4-2 시각
    -입력조건
    첫째 줄에 정수 N이 주어진다(1<=N<=23)
    -출력조건
    00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
'''''
N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            #print("!")
            if(k%10==3 or k//10==3 or j // 10 == 3 or j%10 ==3 or i//10==3 or i%10 ==3 ):
                count +=1
print(count)