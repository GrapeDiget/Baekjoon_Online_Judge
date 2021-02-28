N = int(input())
leap = False
if N % 4 == 0:
    if N % 100 == 0:
        if N % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

if leap:
    print("1")
else:
    print("0")


# 수학
# 구현