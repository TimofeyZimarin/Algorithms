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
                return print('yes')
            else:
                head_elem = head_elem.NextNode
        return print('no')

    def check(self):
        head_elem = self.head
        while head_elem is not None:
            print(head_elem.Node, end=' ')
            head_elem = head_elem.NextNode
        print()
        return

class HashTable():

    def __init__(self):
        self.table = []

    def HashFunc(self, m, s):
        h = 0
        for i in range(len(s)):
            h_temp = (ord(s[i]) * 263 ** i) % 1000000007
            h += h_temp
        h = h % m

def main():
    m = int(input())
    n = int(input())
    req = []
    for i in range(n):
        req.append(input().split())
    print(m, n, req)

main()

# List = LinkedList()
# List.find('aqfas')
# List.delete('aqfasaqfasaqfasaqfas')
# for i in range(5):
#     s = 'aqfas' * i
#     List.add(s)
# List.check()
# List.find('aqfasaqfasaqfas')
# List.delete('aqfas')
# List.add('123421')
# List.find('aqfasaqfasaqfas')
# List.check()
