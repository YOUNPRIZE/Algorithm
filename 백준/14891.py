# 백준 - 구현
## 실버 1
### 톱니바퀴

'''
from itertools import count
import sys
from collections import deque

def clockwise(w):
    w = deque()
    num = w.pop()
    w.appendleft(num)
    return w

def counterclockwise(w):
    w = deque()
    num = w.popleft()
    w.append(num)
    return w

def rightside(n):
    if wheels[n][6] == wheels[n+1][2]:
        if direction == -1:
            clockwise(wheels[n+1])
            direction = 1
        else:
            counterclockwise(wheels[n+1])
            direction = -1
    else:
        None
    
    
        
def leftside(n):
    if wheels[n][2] == wheels[n-1][6]:
        if number == -1:
            clockwise(wheels[n-1])
        else:
            counterclockwise(wheels[n-1])
    else:
        None
        
def check(wheelNumb, direction):
    if direction == 1:
        clockwise(wheels[wheelNumb-1])
    else: 
        counterclockwise(wheels[wheelNumb-1])
    
    if wheelNumb == 1:
        rightside(0)


if __name__ == "__main__":

    wheels = []

    for i in range(4):
        wheels.append(list(sys.stdin.readline()))

    K = int(sys.stdin.readline())

    method = []
    for i in range(K):
        method.append(list(map(int, sys.stdin.readline().split())))
'''
##################################################################################

from collections import deque

circle = [deque(map(int,input())) for _ in range(4)]
opers = deque(list(map(int,input().split())) for _ in range(int(input())))

while opers:	# 명령어가 남아 있으면 반복문 실행
    num,direct = opers.popleft()
    num-=1  # 0 index
    tmp_2 = circle[num][2]	# 비교 대상 백업
    tmp_6 = circle[num][6]	# 비교 대상 백업
    circle[num].rotate(direct)	# 일단 시작 톱니 돌려주기
    tmp_direct=direct
    
    # 시작 톱니 왼쪽 방향
    direct=tmp_direct
    for i in range(num-1,0-1,-1):
        if circle[i][2]!=tmp_6:		# 서로 다른 극인 경우
            tmp_6=circle[i][6]
            circle[i].rotate(direct*-1)
            direct*=-1
        else:
            break

    # 시작 톱니 오른쪽 방향
    direct=tmp_direct
    for i in range(num+1,4):
        if circle[i][6]!=tmp_2:		# 서로 다른 극인 경우
            tmp_2 = circle[i][2]
            circle[i].rotate(direct*-1)
            direct*=-1
        else:
            break

ans=0
for i in range(4):
    if circle[i][0]==1:
        ans += (2**i)
print(ans)
