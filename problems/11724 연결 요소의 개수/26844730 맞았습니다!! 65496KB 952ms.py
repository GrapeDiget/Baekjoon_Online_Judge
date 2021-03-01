import sys
import collections
input = sys.stdin.readline

N, M = map(int, input().split())
edge = collections.defaultdict(list)
for m in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

queue = collections.deque([1])
visited = collections.defaultdict(lambda: False)
n = 1
visited[1] = True
cnt = 1
while queue:
    now = queue.popleft()
    for node in edge[now]:
        if not visited[node]:
            visited[node] = True
            queue.append(node)
    if len(queue) == 0:
        while visited[n]:
            if n >= N:
                break
            n += 1
        else:
            queue.append(n)
            visited[n] = True
            cnt += 1

print(cnt)


# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색
# collections.defaultdict()
# 트리의 개수