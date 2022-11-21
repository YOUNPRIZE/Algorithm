# 백준 - DFS, BFS
## 실버 1
### 단지번호붙이기

import sys
from collections import deque
#input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
homes = []

def bfs(x, y, value):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if N > nx >= 0 and N > ny >= 0:
                if graph[nx][ny] == value and graph[nx][ny] != 0:
                    q.append((nx, ny))
                    cnt += 1
                    graph[nx][ny] = 0
    
    return cnt + 1

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            homes.append(bfs(i,j,graph[i][j]))

homes.sort()

print(len(homes))
for i in range(len(homes)):
    print(homes[i])
