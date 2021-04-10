import sys
import collections
import itertools
import functools
input = sys.stdin.readline

for t in range(int(input())):
    cards = list()
    for m in range(int(input())):
        P, N = map(int, input().rstrip().split())
        for n in range(N):
            cards.append(P)
    y = 0
    origin_sum = sum(cards)
    origin_num = len(cards)
    group = list()
    for i in cards:
        if origin_sum-i == i:
            y = max(y, i)

    for i in range(2, origin_num+1):
        for group in itertools.combinations(cards, i):
            mul = functools.reduce(lambda x, y: x*y, group)
            if origin_sum-sum(group) == mul:
                y = max(y, mul)
            elif origin_sum-sum(group) < mul:
                continue

    print(f"Case #{t+1}: {y}")
