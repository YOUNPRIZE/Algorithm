# 백준 - DFS/BFS
## 실버 1
### 맥주 마시면서 걸어가기

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    beer = 1000
    n = int(input())
    array = []
    for j in range(n+2): 
        array.append(list(map(int, input().split())))
        
    array.sort(key=lambda x : (x[1] + x[0]))
    
    for k in range(1, len(array)):
        beer -= sum(array[k]) - sum(array[k-1])
        
        if beer < 0:
            print('sad')
            break
        
        beer += 1000
    
    if beer < 0:
        break
    
    print('happy')