# 백준 - Greedy
## 골드 5
### 강의실

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

classes = deque()

# 강의 번호, 강의 시작 시간, 강의 종료 시간

for i in range(N):
    classes.append(list(map(int, input().split())))

classes.sort(key=lambda x : x[2])

time = 0

cnt = 0

while len(classes) != 0:
    for i in range(len(classes)):
        if i == 0:
            lec = classes.popleft()
            time = lec[2]
        elif classes[i][2]

print(classes)

# 다시 풀기