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


S = list()
for i in input().rstrip():
    if i.isdigit():
        if len(S) == 0 or not S[-1].isdigit():
            S.append(i)
        else:
            S[-1] += i
    else:
        S[-1] = int(S[-1])
        S.append(i)
S[-1] = int(S[-1])
if len(S) == 1:
    print(S[0])
    exit()

terms = list()
for i in range(1, len(S), 2):
    terms.append([[i], cal(S[i-1], S[i], S[i+1])])
for _ in range(len(terms)-1):
    best = 0
    for t in range(1, len(terms)):
        if terms[t][0] == [-1]:
            continue
        if terms[t][1] > terms[best][1]:
            best = t
        elif terms[t][1] == terms[best][1]:
            if order(S[terms[t][0][0]]) > order(S[terms[best][0][0]]):
                best = t
    if best == 0:
        terms[best+1][1] = cal(terms[best][1],
                               S[terms[best+1][0][0]], S[terms[best+1][0][0]+1])
        terms[best+1][0] += terms[best][0]
    elif best == len(terms)-1:
        terms[best-1][1] = cal(S[terms[best-1][0][0]-1],
                               S[terms[best-1][0][0]], terms[best][1])
        terms[best-1][0] += terms[best][0]
    else:
        terms[best+1][1] = cal(terms[best][1],
                               S[terms[best+1][0][0]], S[terms[best+1][0][0]+1])
        terms[best-1][1] = cal(S[terms[best-1][0][0]-1],
                               S[terms[best-1][0][0]], terms[best][1])
        terms[best+1][0] += terms[best][0]
        terms[best-1][0] += terms[best][0]
    for t in terms[best][0]:
        S[t-1] = terms[best][1]
        S[t+1] = terms[best][1]
    terms[best][0] = [-1]

result = max(terms)[0][0]
print(cal(S[result-1], S[result], S[result+1]))


# 구현
# 자료 구조
# 문자열
# 파싱
# 우선순위 큐
# 트리를 사용한 집합과 맵