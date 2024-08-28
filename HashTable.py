class Node:
    def __init__(self, Node=None):
        self.Node = Node
        self.NextNode = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, s):
        new_s = Node(s)
        if self.head is None:
            self.head = new_s
            return
        else:
            if self.find(s) == 'yes':
                return
            old_s = self.head
            new_s.NextNode = old_s
            self.head = new_s

    def delete(self, s):
        head_elem = self.head
        if head_elem is not None:
            if head_elem.Node == s:
                self.head = head_elem.NextNode
                head_elem = None
                return
            while head_elem is not None:
                if head_elem.Node == s:
                    break
                old = head_elem
                head_elem = head_elem.NextNode
            if head_elem == None:
                return
            old.NextNode = head_elem.NextNode
            head_elem = None

    def find(self, s):
        head_elem = self.head
        while head_elem:
            if head_elem.Node == s:
                return 'yes'
            else:
                head_elem = head_elem.NextNode
        return 'no'

    def check(self):
        head_elem = self.head
        while head_elem is not None:
            print(head_elem.Node, end=' ')
            head_elem = head_elem.NextNode
        print()
        return

class HashTable():

    def __init__(self, m):
        self.table = [None for i in range(m)]
        self. m = m

    def HashFunc(self, s):
        h = 0
        for i in range(len(s)):
            h_temp = (ord(s[i]) * 263 ** i) % 1000000007
            h += h_temp
        h = h % 1000000007 % self.m
        return h

    def add(self, s):
        ind = self.HashFunc(s)
        if self.table[ind] is None:
            self.table[ind] = LinkedList()
            self.table[ind].add(s)
        else:
            self.table[ind].add(s)

    def delete(self, s):
        ind = self.HashFunc(s)
        if self.table[ind] is None:
            return
        else:
            self.table[ind].delete(s)

    def find(self, s):
        ind = self.HashFunc(s)
        if self.table[ind] is None:
            return print('no')
        else:
            print(self.table[ind].find(s))

    def check(self, ind):
        if self.table[ind] is None:
            return
        else:
            self.table[ind].check()

def main():
    m = int(input())
    n = int(input())
    req = []
    Hash = HashTable(m)
    for i in range(n):
        req.append(input().split())
    for i in range(len(req)):
        meth = req[i][0]
        s = req[i][1]
        if meth == 'add':
            Hash.add(s)
        elif meth == 'find':
            Hash.find(s)
        elif meth == 'check':
            Hash.check(int(s))
        elif meth == 'del':
            Hash.delete(s)

main()
