'''''
예제4-3 왕실의 나이트
    -입력조건
    첫째 줄에 정수 N이 주어진다(1<=N<=23)
    -출력조건
    00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
'''''
loc = str(input())

char = loc[0:1]
num = int(loc[1:2])

if (char > 'b' and char < 'g' and num > 2 and num <9):
    print ("8")
elif(char == 'b' and num > 1 and num <8):
    print("4")
elif(char == 'g' and num > 1 and num <8):
    print("4")
elif(num == '2'and char > 'a' and char < 'h'):
    print("4")
elif(num == '7'and char > 'a' and char < 'h'):
    print("4")
elif(char == 'a' and num > 2 and num <7):
    print("4")
elif(char == 'h' and num > 2 and num <7):
    print("4")
elif(num == '1'and char > 'b' and char < 'g'):
    print("4")
elif(num == '8'and char > 'b' and char < 'g'):
    print("4")
elif(char == 'a' and num == 2):
    print("3")
elif (char == 'a' and num == 7):
    print("3")
elif (char == 'b' and num == 1):
    print("3")
elif (char == 'b' and num == 8):
    print("3")
elif (char == 'g' and num == 1):
    print("3")
elif (char == 'g' and num == 8):
    print("3")
elif (char == 'h' and num == 2):
    print("3")
elif (char == 'h' and num == 7):
    print("3")
else:
    print("2")
