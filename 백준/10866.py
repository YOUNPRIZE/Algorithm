# 백준 - 덱
## 실버 4
### 덱

# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque
N = int(sys.stdin.readline())

array = []

for i in range(N):
    order = sys.stdin.readline().strip()
    array.append(order)
    
deq = deque()

for i in array:
    if i == "pop_front":
        if len(deq) > 0:
            numb = deq.popleft()
            print(numb)
        else:
            print(-1)
    elif i == "pop_back":
        if len(deq) > 0:
            numb = deq.pop()
            print(numb)
        else:
            print(-1)
    elif i == "size":
        print(len(deq))
    elif i == "empty":
        if len(deq) > 0:
            print(0)
        else:
            print(1)
    elif i == "front":
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    elif i == "back":
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)
    elif "push_front" in i:
        deq.appendleft(i[11:])
    else:
        deq.append(i[10:])