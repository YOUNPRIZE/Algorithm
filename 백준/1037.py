# 백준 - 구현
## 실버 5
### 약수

# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

#import sys

#N = int(sys.stdin.readline())

N = int(input())

yaksu = list(map(int, input().split()))

answer = min(yaksu) * max(yaksu)

print(answer)
