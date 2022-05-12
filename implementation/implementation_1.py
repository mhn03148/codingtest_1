'''''
예제4-1 상하좌우
    -입력조건
    첫째 줄에 공간의 크기를 나타내는 N이 주어진다(1<=N<=100)
    둘쩨 줄에 여행가 A 이동할 계획서 내용이 주어진다. (1<=이동횟수<=100)    
    -출력조건
    첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백으로 구분하여 출력한다.
'''''

N = input()
Lord = list(map(str, input().split()))
x, y = 1,1

for i in Lord:
    if(i == 'U'):
        if(x==1):
            x=x
        else:
            x-=1
    elif(i == 'D'):
        if(x==N):
            continue
        else:
            x+=1
    elif (i == 'R'):
        if (y == N):
            continue
        else:
            y += 1
    elif (i == 'L'):
        if (y == 1):
            continue
        else:
            y -= 1

print(x, y)