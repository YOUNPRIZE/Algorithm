# 백준 - Greedy
## 골드 5
### 지뢰찾기

import sys

input = sys.stdin.readline

T = int(input())

cases = []

for _ in range(T):
    N = int(input())
    case = []
    case.append(int(input()))
    case.append(input().strip())
    cases.append(case)
