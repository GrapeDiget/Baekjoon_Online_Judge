import sys
input = sys.stdin.readline


def order(x):
    if x == '+':
        return 0
    elif x == '-':
        return 0
    elif x == '*':
        return 1
    elif x == '/':
        return 1


def cal(a, oper, b):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b
    elif oper == '/':
        return a//b


class Term:
    def __init__(self, idx, left, oper, right):
        self.hidx = None
        self.idx = idx
        self.left = left
        self.oper = oper
        self.right = right
        self.result = None
        self.leftlink = None
        self.rightlink = None
        self.isvalid = True
        self.update()

    def __str__(self):
        result = f'h:{self.hidx}, l:{self.left}, r:{self.right}, s:{self.result}, v:{self.isvalid}'
        if self.leftlink != None:
            result += f' ll:{self.leftlink.idx}'
        if self.rightlink != None:
            result += f' rl:{self.rightlink.idx}'
        return result

    def __repr__(self):
        return self.__str__()

    def update(self):
        self.result = cal(self.left[0], self.oper, self.right[0])


heap = [None] * 100001
heap_size = 0
def parent(i): return heap[i//2]
def lchild(i): return heap[i*2]
def rchild(i): return heap[i*2+1]
def find_heap(): return heap[1]


def verdict(low, high):
    if low.result > high.result:
        return True
    elif low.result == high.result:
        if order(low.oper) > order(low.oper):
            return True
        elif order(low.oper) == order(low.oper):
            if low.idx < high.idx:
                return True
    return False


def insert_heap(node):
    global heap_size, heap
    heap_size += 1
    i = heap_size
    while i != 1 and verdict(node, parent(i)):
        parent(i).hidx = i
        heap[i] = parent(i)
        i //= 2
    node.hidx = i
    heap[i] = node


def delete_heap():
    global heap_size, heap
    parent = 1
    child = 2
    best = heap[1]

    # 얻은 best의 값 변경
    best.isvalid = False
    best.left[0] = best.result
    best.right[0] = best.result

    # best의 left와 right의 값이 변했으므로 left_term과 right_term을 갱신하고 힙에서 제거
    left_term = best.leftlink
    if left_term != None:
        while not left_term.isvalid:
            left_term = left_term.leftlink
            if left_term == None:
                best.leftlink = left_term
                break
        else:
            best.leftlink = left_term
            left_term.rightlink = best
            left_term.right = best.left
            update_heap(left_term)

    right_term = best.rightlink
    if right_term != None:
        while not right_term.isvalid:
            right_term = right_term.rightlink
            if right_term == None:
                best.rightlink = right_term
                break
        else:
            best.rightlink = right_term
            right_term.leftlink = best
            right_term.left = best.right
            update_heap(right_term)

    # best를 제거하고 힙을 재정렬
    last = heap[heap_size]
    heap_size -= 1
    while child <= heap_size:
        if child < heap_size and not verdict(lchild(parent), rchild(parent)):
            child += 1
        if verdict(last, heap[child]):
            break
        heap[child].hidx = parent
        heap[parent] = heap[child]
        parent = child
        child *= 2
    last.hidx = parent
    heap[parent] = last

    # best를 제거한 후 left_term과 right_term을 다시 입력
    if left_term != None:
        insert_heap(left_term)
    if right_term != None:
        insert_heap(right_term)


def update_heap(node):
    global heap_size, heap
    node.update()
    parent = node.hidx
    child = parent*2
    last = heap[heap_size]
    heap_size -= 1
    while child <= heap_size:
        if child < heap_size and not verdict(lchild(parent), rchild(parent)):
            child += 1
        if verdict(last, heap[child]):
            break
        heap[child].hidx = parent
        heap[parent] = heap[child]
        parent = child
        child *= 2
    last.hidx = parent
    heap[parent] = last


if __name__ == '__main__':
    number = ''
    S = list()
    for i in input().rstrip():
        if i.isdigit():
            number += i
        else:
            S.append([int(number)])
            number = ''
            S.append(i)
    S.append([int(number)])
    if len(S) == 1:
        print(S[0][0])
        exit()

    heap_size = 0
    # 항들을 저장하는 리스트 생성
    terms = list()
    for i in range(1, len(S), 2):
        terms.append(Term(i, S[i-1], S[i], S[i+1]))

    # 항들을 힙에 입력
    terms[0].rightlink = terms[1]
    insert_heap(terms[0])
    for t in range(1, len(terms)-1):
        terms[t].leftlink = terms[t-1]
        terms[t].rightlink = terms[t+1]
        insert_heap(terms[t])
    terms[len(terms)-1].leftlink = terms[len(terms)-2]
    insert_heap(terms[len(terms)-1])

    # 힙에 1개만 남을 때 까지 추출
    while heap_size > 1:
        best = delete_heap()

    print(heap[1].result)


# 구현
# 자료 구조
# 문자열
# 파싱
# 우선순위 큐
# 트리를 사용한 집합과 맵
# 연결 리스트
# 클래스
# 메인 구절