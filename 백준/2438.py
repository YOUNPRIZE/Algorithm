# 백준 - 구현
## 브론즈 3
### 별 찍기 - 1

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

import sys

N = int(sys.stdin.readline())

for i in range(N):
    star = "*" * (i + 1)
    print(star)
    
