# 백준 다이나믹 프로그래밍
## 크리보드

'''
import sys

N = int(sys.stdin.readline())

dp = [0] * (N)

dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 2, 3, 4, 5, 6

#1 2 3 4 5 6 (7 8) 9 10 11

#1 2 3 4 5 6 (9 12) 16 20 27  

for i in range(6, N+1):



3 + (3 * 2)
3 + (3 * 3)
3 + (3 * 4)
4 + (4 * 3)
4 + (4 * 4)

3 + (3 * 2)
'''

import sys
input = sys.stdin.readline
n = int(input())
dp = [i for i in range(0, 102)]

for i in range(6, 101):
    dp[i] = max(dp[i-3]*2, max(dp[i-4]*3, dp[i-5]*4))
print(dp[n])

