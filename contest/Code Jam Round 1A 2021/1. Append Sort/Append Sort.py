import sys
input = sys.stdin.readline

for t in range(int(input())):
    int(input())
    L = list(input().rstrip().split())
    y = 0
    for i in range(1, len(L)):
        before = L[i-1]
        now = L[i]
        if int(before) < int(now):
            continue
        elif len(before) == len(now):
            now += '0'
            y += 1
        else:
            before_part = int(before[:len(now)])
            if before_part > int(now):
                for j in range(len(before)-len(now)+1):
                    now += '0'
                    y += 1
            elif before_part < int(now):
                for j in range(len(before)-len(now)):
                    now += '0'
                    y += 1
            else:
                if int(str(int(before)+1)[:len(now)]) == before_part:
                    y += len(before)-len(now)
                    now = str(int(before)+1)
                else:
                    for j in range(len(before)-len(now)+1):
                        now += '0'
                        y += 1
        L[i] = now

    print(f"Case #{t+1}: {y}")
