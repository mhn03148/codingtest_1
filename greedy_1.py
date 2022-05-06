N, M, K = map(int,(input().split()))
data = list(map(int,input().split()))
data.sort(reverse=True)

n = (M % (K+1))
m = (M // (K+1))

sum = ((m * (data[0] * K + data[1])) + ((data[0]) * n))
print (sum)
