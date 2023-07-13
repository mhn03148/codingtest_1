import sys
from collections import deque
input = sys.stdin.readline
Testcase = int(input().strip())
for i in range(Testcase):
    func = ""
    numArray = []
    func = input().strip()
    num = int(input().strip())
    numArray = list(map(str,input().strip()[1:-1].split(",")))
    dq = deque(numArray)
    flag = 0
    back = False

    if num == 0:
        dq = []

    for j in func:
        if j == "R":
            if back == True:
                back = False
            else:
                back = True
        elif j == "D":
            if len(dq) < 1:
                flag = 1
                print("error")
                break
            else:
                if back == False:
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 0:
        if back == False:
            # return numArray
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            # return numArray[::-1]
            print("[" + ",".join(dq) + "]")






'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''