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
terms = list()
while len(S) > 1:
    terms.clear()
    for i in range(1, len(S), 2):
        oper = S[i]
        if oper == '+':
            terms.append((i, S[i-1]+S[i+1]))
        elif oper == '-':
            terms.append((i, S[i-1]-S[i+1]))
        elif oper == '*':
            terms.append((i, S[i-1]*S[i+1]))
        elif oper == '/':
            terms.append((i, S[i-1]//S[i+1]))
    terms.sort(key=lambda x: -x[1])
    best = terms[0]
    if len(terms) > 1 and terms[0][1] == terms[1][1]:
        for i in range(1, len(terms)):
            if terms[i][1] == best[1]:
                break
            if order(S[terms[i][0]]) > order(S[best[0]]):
                best = terms[i]
            i += 1
    S[best[0]] = best[1]
    S.pop(best[0]-1)
    S.pop(best[0])

print(S[0])
