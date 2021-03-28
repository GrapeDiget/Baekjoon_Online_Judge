import sys
input = sys.stdin.readline

for t in range(int(input())):
    X, Y, S = input().rstrip().split()
    X = int(X)
    Y = int(Y)
    mul = list()
    for s in S:
        if s != '?':
            mul.append(s)
    cost = 0
    for i in range(1, len(mul)):
        if (mul[i-1], mul[i]) == ('C', 'J'):
            cost += X
        elif (mul[i-1], mul[i]) == ('J', 'C'):
            cost += Y

    print(f"Case #{t+1}: {cost}")
