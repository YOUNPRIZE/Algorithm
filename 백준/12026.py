# 백준 다이나믹 프로그래밍
## BOJ 거리
### 모르겠음..

import sys
n=int(sys.stdin.readline())
block=sys.stdin.readline()

# 무조건 pass 해야 되는 경우: B 다음에 O가 나오지 않는 경우
# o가 연속적으로 나오는 경우

dp=[float('inf')]*(n+1)

# B이면 O를 만났을 때 종료, O이면 J를 만날 때까지, J이면 B를 만날 때까지
def get_prev(x):
    if x=='B':
        return 'J'
    elif x=='J':
        return 'O'
    elif x=='O':
        return 'B'
dp[0]=0
for i in range(1,n):
    prev=get_prev(block[i])
    for j in range(i):
        if block[j]==prev: # b다음에 o 식으로 들어왔을 때 
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))

print(dp[n-1] if dp[n-1] !=float('inf') else -1)