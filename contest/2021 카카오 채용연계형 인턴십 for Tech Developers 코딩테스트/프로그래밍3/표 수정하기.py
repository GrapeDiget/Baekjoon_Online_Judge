class Node:
    def __init__(self, idx, n):
        if idx == 0:
            self.parent = None
        else:
            self.parent = idx-1
        self.idx = idx
        if idx == n-1:
            self.child = None
        else:
            self.child = idx+1
        self.isValid = True

    def __str__(self):
        result = f'p = {self.parent}, i = {self.idx}, c = {self.child}, {self.isValid}'
        return result

    def __repr__(self):
        return self.__str__()


def solution(n, k, cmd):
    table = list()
    undolist = list()
    answer = ''

    for N in range(n):
        table.append(Node(N, n))

    for i in cmd:
        if i == 'C':
            if table[k].parent == None:
                table[table[k].child].parent = table[k].parent
                table[k].isValid = False
                undolist.append(k)
                k = table[k].child
            elif table[k].child == None:
                table[table[k].parent].child = table[k].child
                table[k].isValid = False
                undolist.append(k)
                k = table[k].parent
            else:
                table[table[k].parent].child = table[k].child
                table[table[k].child].parent = table[k].parent
                table[k].isValid = False
                undolist.append(k)
                k = table[k].child
        elif i == 'Z':
            undo = undolist.pop()
            table[undo].isValid = True
            if table[undo].parent == None:
                table[table[undo].child].parent = undo
            elif table[undo].child == None:
                table[table[undo].parent].child = undo
            else:
                table[table[undo].parent].child = undo
                table[table[undo].child].parent = undo
        else:
            way, x = i.split()
            x = int(x)
            if way == 'U':
                for X in range(x):
                    k = table[k].parent
            elif way == 'D':
                for X in range(x):
                    k = table[k].child

    for count in table:
        if count.isValid:
            answer += 'O'
        else:
            answer += 'X'

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C",
                      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
