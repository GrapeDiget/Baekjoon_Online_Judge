T = int(input())
for t in range(T):
    string = input()
    before = list()
    after = list()
    for s in string:
        if s == '-':
            if before:
                before.pop()
        elif s == '<':
            if before:
                after.append(before.pop())
        elif s == '>':
            if after:
                before.append(after.pop())
        else:
            before.append(s)
    for s in before:
        print(s, end="")
    while after:
        print(after.pop(), end="")
    print()


# 스택