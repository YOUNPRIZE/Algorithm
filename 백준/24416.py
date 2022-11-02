# 백준 - DP
## 브론즈 1
### 알고리즘 수업 - 피보나치 수 1

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    f = [0]*(n+1)
    f[1], f[2] = 1, 1
    count = 0
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return count

n = int(input())

print(fib(n), fibonacci(n))
