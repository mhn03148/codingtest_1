N, M = map(int,input().split())
money_set = []
money_sol = []
ans_list=[]
i = 0
ans = 0
for i in range(M):
    a, b = map(int,input().split())
    money_set.append(a)
    money_sol.append(b)

ans = N // 6
i = N % 6

ans_list.append(min(money_set)*(ans+1))
ans_list.append(min(money_set)*ans + min(money_sol)*(i))
ans_list.append(min(money_sol)*N)

print(min(ans_list))