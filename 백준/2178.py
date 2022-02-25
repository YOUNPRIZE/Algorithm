# 백준 - BFS
## 실버 1
### 미로 탐색

# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0 1	1 1	1
# 1	0 1	0 1	0
# 1	0 1	0 1	1
# 1	1 1	0 1	1

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
# 각각의 수들은 붙어서 입력으로 주어진다.

'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

puzzle = []

for i in range(n):
    puzzle.append(list(sys.stdin.readline().strip()))
    
# BFS
def bfs(x, y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이므로 진행 불가
            if puzzle[nx][ny] == 0:
                puzzle[nx][ny] = puzzle[x][y] + 1
                queue.append((nx, ny))
    
            # 벽이 아니므로 이동
            if puzzle[nx][ny] == 1:
                puzzle[nx][ny] = puzzle[x][y] + 1
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return puzzle[n-1][m-1]

print(bfs(0, 0))            
'''
n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
            queue.append([x, y])
            s[x][y] = s[a][b] + 1
print(s[n - 1][m - 1])

#0, 0부터 bfs를 이용해 동, 서, 남, 북을 검사하여 "1"인 값을 찾는다.

 

#만약 "1"이라면 기준이 되는 숫자에 +1을 하여 값을 넣어준다.

 

#이렇게 쭉 검사를 해나가면 마지막 s[n - 1, m - 1]에는 최솟값이 들어가게 된다.