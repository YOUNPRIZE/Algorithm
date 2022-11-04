# 백준 - DP
## 실버 2
### 가장 긴 증가하는 부분 수열

from sys import stdin

N = int(stdin.readline())

A = map(int, stdin.readline().split())

dp = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))