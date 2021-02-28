str = input().upper()
set_str = list(set(str))
max_char = '?'
max_num = 0
for i in range(len(set_str)):
    if str.count(set_str[i]) > max_num:
        max_num = str.count(set_str[i])
        max_char = set_str[i]
    elif str.count(set_str[i]) == max_num:
        max_num = str.count(set_str[i])
        max_char = '?'
    else:
        pass

print(max_char)


# 구현
# 문자열
# collections.Counter