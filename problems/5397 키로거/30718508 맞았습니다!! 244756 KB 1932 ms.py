class Node:
    def __init__(self, data):
        self.data = data
        self.prevLink = None
        self.nextLink = None

    def __repr__(self) -> str:
        return f"data: {self.data}"


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.now = self.head

    def deletePrev(self):
        if self.now.prevLink == None:
            return
        self.now.prevLink.nextLink = self.now.nextLink
        if self.now.nextLink != None:
            self.now.nextLink.prevLink = self.now.prevLink
        self.now = self.now.prevLink

    def goLeft(self):
        if self.now.prevLink != None:
            self.now = self.now.prevLink

    def goRight(self):
        if self.now.nextLink != None:
            self.now = self.now.nextLink

    def add(self, data):
        new = Node(data)
        new.prevLink = self.now
        new.nextLink = self.now.nextLink
        if self.now.nextLink != None:
            self.now.nextLink.prevLink = new
        self.now.nextLink = new
        self.now = self.now.nextLink

    def printList(self):
        now = self.head.nextLink
        while now != None:
            print(now.data, end="")
            now = now.nextLink
        print("")


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        string = input()
        myList = LinkedList()
        for s in string:
            if s == '-':
                myList.deletePrev()
            elif s == '<':
                myList.goLeft()
            elif s == '>':
                myList.goRight()
            else:
                myList.add(s)
        myList.printList()


# 연결 리스트