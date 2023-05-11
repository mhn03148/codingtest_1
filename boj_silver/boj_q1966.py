T = int(input())
ans = []
for _ in range(T):
    N,M = map(int, input().split())
    pri=list(map(int,input().split()))
    print_arr = []
    for i in range(N):
        print_arr.append((pri[i],i))
    count = 0
    while print_arr:
        if len(print_arr)>0:
            if print_arr[0][0] < max(print_arr)[0]:
                a = print_arr.pop(0)
                print_arr.append(a)
            else:
                count+=1
                if print_arr[0][1] == M:
                    ans.append(count)
                    break
                print_arr.pop(0)

for i in ans:
    print(i, end="\n")
