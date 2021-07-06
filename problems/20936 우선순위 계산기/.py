import operator
import sys
import collections
input = sys.stdin.readline


STR2FUNC = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv,
    '*': operator.mul,
}

OPERATOR_ORDER = {
    operator.add: 0,
    operator.sub: 0,
    operator.floordiv: 1,
    operator.mul: 1,
}


# 항을 나타내는 클래스
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
        self.update()

    # 항의 결과값을 업데이트
    def update(self):
        self.result = self.oper(self.left, self.right)


# 힙 구성
heap = [None] * 100001
heap_size = 0

# term_A가 term_B보다 우선순위가 높으면 True를 출력, 아니면 False를 출력
def verdict(term_A, term_B):
    if term_A.result > term_B.result:
        return True
    if term_A.result == term_B.result:
        if OPERATOR_ORDER[term_A.oper] > OPERATOR_ORDER[term_B.oper]:
            return True
        if OPERATOR_ORDER[term_A.oper] == OPERATOR_ORDER[term_B.oper]:
            if term_A.idx < term_B.idx:
                return True
    return False

# 힙에 노드를 삽입
def insert_heap(node):
    global heap_size, heap
    heap_size += 1
    i = heap_size
    while i != 1 and verdict(node, heap[i//2]):
        heap[i//2].hidx = i
        heap[i] = heap[i//2]
        i //= 2
    node.hidx = i
    heap[i] = node

# 현재 힙에 저장된 값 중 우선순위가 가장 높은 노드를 삭제
# 그 노드의 삭제로 인해 발생하는 좌항과 우항의 변화를 감지 및 반영
def delete_heap():
    global heap_size, heap
    # best를 구한 뒤 힙에서 제거하기 위해 백업 및 유효하지 않도록 수정
    best = heap[1]

    # best의 변화를 left_term과 right_term에 적용하고 둘을 연결, 힙에서의 위치를 수정
    left_term = best.leftlink
    right_term = best.rightlink
    if left_term != None:
        left_term.rightlink = right_term
        left_term.right = best.result
        update_heap(left_term)
    if right_term != None:
        right_term.leftlink = left_term
        right_term.left = best.result
        update_heap(right_term)

    # best를 제거하고 힙을 재정렬
    last = heap[heap_size]
    heap[heap_size] = None
    heap_size -= 1
    parent = 1
    child = 2
    while child <= heap_size:
        if child < heap_size and not verdict(heap[parent*2], heap[parent*2+1]):
            child += 1
        if verdict(last, heap[child]):
            break
        heap[child].hidx = parent
        heap[parent] = heap[child]
        parent = child
        child *= 2
    last.hidx = parent
    heap[parent] = last
    best.hidx = None

# 힙 중간에 있는 노드의 위치를 조정
def update_heap(node):
    global heap_size, heap
    node.update()
    i = node.hidx

    # 부모노드보다 우선순위가 높으면 up heap
    if i > 3 and verdict(node, heap[i//2]):
        while i > 3 and verdict(node, heap[i//2]):
            heap[i//2].hidx = i
            heap[i] = heap[i//2]
            i //= 2
        node.hidx = i
        heap[i] = node
        return

    # 자식노드보다 우선순위가 낮으면 down heap
    child = i*2
    while child <= heap_size:
        if child < heap_size and not verdict(heap[i*2], heap[i*2+1]):
            child += 1
        if verdict(node, heap[child]):
            break
        heap[child].hidx = i
        heap[i] = heap[child]
        i = child
        child *= 2
    node.hidx = i
    heap[i] = node


if __name__ == '__main__':
    number = ''
    S = list()
    for i in input().rstrip():
        if i.isdigit():
            number += i
        else:
            S.append(int(number))
            number = ''
            S.append(STR2FUNC[i])
    S.append(int(number))
    if len(S) == 1:
        print(S[0])
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
    
    heap = collections.deque(heap[1:heap_size+1])
    
    best = heap[0]
    
    





    # 힙에 1개만 남을 때 까지 추출
    while heap_size > 1:
        delete_heap()

    print(heap[1].result)
