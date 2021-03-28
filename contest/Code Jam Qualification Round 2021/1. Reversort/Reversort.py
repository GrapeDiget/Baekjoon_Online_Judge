import sys
input = sys.stdin.readline

for t in range(int(input())):
    int(input())
    L = list(map(int, input().rstrip().split()))
    cost = 0
    for i in range(len(L)-1):
        key = min(L[i:])
        if L[i] >= key:
            j = L.index(key)
            cost += (j+1)-(i+1)+1
            L[i:j+1] = reversed(L[i:j+1])

    print(f"Case #{t+1}: {cost}")
