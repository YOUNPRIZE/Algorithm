# 백준 - DFS, BFS
## 실버 2
### DFS와 BFS

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

# DFS => 스택 or 재귀
# BFS => 큐

from collections import deque
import sys

def bfs(v):
    q = deque()
    q.append(v)       
    visited[v] = 1   
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

def dfs(v):
    # 방문한 곳은 1 넣기
    visited[v] = 1 
    
    print(v, end = " ")
    
    # 재귀 함수 선언 (V와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)
    for i in range(1, n + 1):
        if visite[i] == 0 and graph[v][i] == 1:
            dfs(i)

if __name__ == "__main__":
    # 입력 변수 받기
    n, m, v = map(int, sys.stdin.readline().split())

    # 인접 영행령 생성
    graph = [[0] * (n + 1) for _ in range(n + 1)] 
    
    # 방문한 곳 체크를 위한 배열 선언
    visited = [0] * (n + 1)

    # 입력 받는 두 값에 대해 영행렬에 1 삽입
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = graph[b][a] = 1

    dfs(v)
    print()
    bfs(v)