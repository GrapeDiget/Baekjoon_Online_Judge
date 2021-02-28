max_num = 0
max_order = 0
for i in range(1, 10):
    number = int(input())
    if number >= max_num:
        max_num = number
        max_order = i
print(max_num)
print(max_order)


# 구현