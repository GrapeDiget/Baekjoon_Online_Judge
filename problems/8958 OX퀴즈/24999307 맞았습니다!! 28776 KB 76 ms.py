def solve(string):
    pnt = 0
    combo = 0
    for j in string:
        if j == 'O':
            pnt += 1 + combo
            combo += 1
        else:
            combo = 0
    return pnt


n = int(input())
for i in range(n):
    str = input()
    point = solve(str)
    print(point)


# 구현
# 문자열