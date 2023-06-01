N, K = map(int,input().split())
t = 0
arr=[]
ans = []
for i in range(N):
    arr.append(i+1)
#arr = [1,2,3,4,5,6,7]
while arr:
    for i in range(K-1):
        arr.append(arr.pop(0)) #맨 앞부터 차례대로 배열의 뒤로 보냄
    ans.append(arr.pop(0))# 해당하는 배열의 0번째 값을 정답 배열에 추가하고, 원래 배열에서 삭제 시킴

s = str(ans)
s = s[1:]
s = s[:-1]
s = "<" + s + ">"
print(s)

