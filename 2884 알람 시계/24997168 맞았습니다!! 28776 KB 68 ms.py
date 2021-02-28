H, M = map(int, input().split())
set_H = 0
set_M = 0
if M >= 45:
    set_H = H
    set_M = M - 45
elif H >= 1:
    set_H = H - 1
    set_M = M + 60 - 45
elif H == 0:
    set_H = 23
    set_M = M + 60 - 45

print(set_H, set_M)


# 수학
# 사칙연산