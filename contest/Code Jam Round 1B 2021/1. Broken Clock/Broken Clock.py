import sys
import itertools
input = sys.stdin.readline

for t in range(int(input())):
    tick = list(map(int, input().split()))
    h, m, s, n = 0, 0, 0, 0
    found = False

    for A, B, C in itertools.permutations(tick):
        for k in range(0, 60):
            mod = A%720000000000
            if mod:
                A -= mod
                if A < 0:
                    A += 43200000000000
                B -= mod
                if B < 0:
                    B += 43200000000000
                C -= mod
                if C < 0:
                    C += 43200000000000

            sec = A//720000000000
            for i in range(0, 60):
                min = i*720000000000+sec*12000000000
                if B == min:
                    for j in range(0, 12):
                        hour = j*3600000000000+i*60000000000+sec*1000000000
                        if C == hour:
                            h, m, s, n = j, i, sec, mod
                            found = True
                            break
                if found:
                    break
            if found:
                break

            A -= 720000000000
            if A < 0:
                A += 43200000000000
            B -= 720000000000
            if B < 0:
                B += 43200000000000
            C -= 720000000000
            if C < 0:
                C += 43200000000000
        if found:
            break

    print(f"Case #{t+1}: {h} {m} {s} {n}")
