import heapq

N = int(input())
A = map(int, input().split())
heap = []
for a in A:
    heapq.heappush(heap, a)

ans = 0
for n in range(N):
    if ans+1 != heapq.heappop(heap):
        break
    else:
        ans += 1
print(ans+1)


# # 자료 구조
# 우선순위 큐
# heap
# 힙
# heapq