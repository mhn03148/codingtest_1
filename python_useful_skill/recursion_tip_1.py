#피보나치 수열
def solution(n):
    d = [0] * 100000

    def fibo(x):
        if x == 1 or x == 2:
            return 1
        if d[x] != 0:
            return d[x]
        d[x] = fibo(x - 1) % 1234567 + fibo(x - 2) % 1234567
        return d[x] % 1234567

    answer = fibo(n)
    return answer
