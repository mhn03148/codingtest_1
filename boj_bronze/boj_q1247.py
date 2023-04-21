from sys import stdin
ans_list = []
for i in range(3):
    t = int(stdin.readline())
    ansP = 0
    ansM = 0
    for j in range(t):
        if ansP >= 0:
            ansP = ansP + int(stdin.readline())
        else:
            ansM = ansM + int(stdin.readline())
    if ansP > (-1)*ansM :
        ans_list.append("+")
    elif ansP == (-1)*ansM:
        ans_list.append("0")
    else:
        ans_list.append("-")

for i in range(len(ans_list)):
    print(ans_list[i], end='\n')