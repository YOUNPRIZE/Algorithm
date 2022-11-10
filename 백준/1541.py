# 백준 - 그리디
## 실버 2
### 잃어버린 괄호

import sys
input = sys.stdin.readline
string = input().split('-')
num = []
for i in string:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)