# 백준 - 그리디
## 브론즈 2
### 5와 6의 차이

A, B = map(int, input().split())

maxA = str(A).replace('5', '6')
minA = str(A).replace('6', '5')

maxB = str(B).replace('5', '6')
minB = str(B).replace('6', '5')

max = int(maxA) + int(maxB)
min = int(minA) + int(minB)

print(min, max)