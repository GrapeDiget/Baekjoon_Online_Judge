N = int(input())
points = list(map(int, input().split()))
M = max(points)
for i in range(N):
    points[i] = points[i]/M*100
print(sum(points)/N)


# 수학
# 사칙연산
# 주작