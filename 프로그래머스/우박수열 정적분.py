def suggestion(num):
    list = []
    list.append(num)
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        list.append(num)
    return list

def solution(k, ranges):
    answer = []
    list = suggestion(k)
    length = len(list) - 1
    for i in ranges:
        if (length + i[1]) == i[0] :
            answer.append(0.0)
        elif (length + i[1] - i[0]) < 1:
            answer.append(-1.0)
        elif (length + i[1] - i[0]) > 1:
            a = i[0]
            b = length + i[1]
            area = 0
            while a != b:
                down = list[a]
                up = list[a+1]
                area = area + (up + down) / 2
                a += 1
            answer.append(area)
        else:
            down = list[i[0]]
            up = list[length + i[1]]
            area = ((up + down) * (length + i[1] - i[0])) / 2
            answer.append(area)
    return answer