# 백준 - DP
## 브론즈 1
### 부녀회장이 될테야

t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    
    people = [i for i in range(1, num+1)]

    for x in range(floor):
        for y in range(1, num):
            people[y] += people[y-1]
    print(people[-1])