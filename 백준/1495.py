# 백준 다이나믹 프로그래밍
## 기타리스트

'''
import sys
# N 은 공연에서 연주할 곡의 개수
# S 시작 볼륨
# M 
N, S, M = map(int, input().split())

vol = list(map(int, input().split()))

dp = [0] * N

if vol[0] + S <= M:
    dp[0] = vol[0] + S
elif vol[0] + S > M and S - vol[0] >= 0:
    dp[0] = S - vol[0]
else: dp[0] = -1

for i in range(1, N):
    if dp[i-1] == -1: 
        print(dp[i-1])
        break
    elif dp[i-1] + vol[i] <= M:
        dp[i] = dp[i-1] + vol[i]
    elif dp[i-1] + vol[i] > M and dp[i-1] - vol[i] >= 0 and dp[i-1] >= dp[i-1] - vol[i]:
        dp[i] = dp[i-1]
    elif dp[i-1] + vol[i] > M and dp[i-1] - vol[i] >= 0 and dp[i-1] < dp[i-1] - vol[i]:
        dp[i] = dp[i-1] - vol[i]
    elif i == N - 1:
        print(dp[-1])
    else:
        dp[i] = -1

'''

n, s, m = map(int, input().split()) 
v = list(map(int, input().split())) 
dp = [[0] * (m+1) for _ in range(n+1)] 
dp[0][s] = 1 

for i in range(n): 
    for j in range(m+1): 
        if dp[i][j] == 1: 
            if j+v[i] <= m: 
                dp[i+1][j+v[i]] = 1 
            if j-v[i] >= 0:
                dp[i+1][j-v[i]] = 1 
                
ans = -1
for i in range(m, -1, -1): 
    if dp[n][i]==1: 
        ans = i 
        break 

print(ans)

