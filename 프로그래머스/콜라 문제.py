def solution(a, b, n):
    answer = 0
    while n >= a:
        takeCola = n // a
        n = n - (takeCola * a)
        answer += takeCola * b
        n = n + takeCola * b
    return answer