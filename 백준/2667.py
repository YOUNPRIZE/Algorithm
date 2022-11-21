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


# DFS 풀이
'''
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
'''