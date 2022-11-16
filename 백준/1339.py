# 백준 - 그리디
## 골드 4
### 단어 수학

import sys
input = sys.stdin.readline

word = []
numb = { 0 : None, 1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None, 9 : None }
N = int(input())

for i in range(N):
    word.append(input().strip())

word.sort(key=len, reverse=True)

