N = int(input())
in_map=[[0]*N for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(N):
        in_map[i][j] = s[j]

ans_map = [[0]*N for _ in range(N)]
x = [0,1,1,1,0,-1,-1,-1]
y = [1,1,0,-1,-1,-1,0,1]

for i in range(N):
    for j in range(N):
        if in_map[i][j] == ".":
            continue
        else:
            ans_map[i][j] = '*'
            for k in range(8):
                dx = i + x[k]
                dy = j + y[k]
                if dx>-1 and dy>-1 and dx<N and dy<N:
                    if ans_map[dx][dy] == 'M' or ans_map[dx][dy]=="*":
                        continue
                    else:
                        ans_map[dx][dy] = ans_map[dx][dy]+ int(in_map[i][j])
                        if ans_map[dx][dy] > 9:
                            ans_map[dx][dy] = 'M'

for i in range(len(ans_map)):
    for j in range(len(ans_map)):
        print(ans_map[i][j], end="")
    print(end="\n")