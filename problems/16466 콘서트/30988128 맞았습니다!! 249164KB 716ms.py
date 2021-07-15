heap = [None]


def parent(idx: int) -> int:
    return idx//2


def left(idx: int) -> int:
    return idx*2


def right(idx: int) -> int:
    return idx*2+1


def heapSize() -> int:
    return len(heap)-1


def initHeap() -> None:
    global heap
    heap = [None]


def insert(data: int) -> None:
    global heap
    heap.append(None)
    now = heapSize()
    # Upheap!
    while now != 1 and data < heap[parent(now)]:
        heap[now] = heap[parent(now)]
        now = parent(now)
    heap[now] = data


def delete() -> int:
    if heapSize() == 0:
        print("공백 힙 삭제 시도")
        exit()
    global heap
    if heapSize() == 1:
        return heap.pop()
    root = heap[1]
    last = heap.pop()
    parent = 1
    child = 2
    # Downheap!
    while child <= heapSize():
        if child < heapSize() and heap[right(parent)] < heap[left(parent)]:
            child += 1
        if last <= heap[child]:
            break
        heap[parent] = heap[child]
        parent = child
        child = left(child)
    heap[parent] = last
    return root


if __name__ == '__main__':
    N = int(input())
    A = map(int, input().split())
    for n in A:
        insert(n)

    ans = 0
    for n in range(N):
        if ans+1 != delete():
            break
        else:
            ans += 1
    print(ans+1)


# 자료 구조
# 우선순위 큐
# heap
# 힙