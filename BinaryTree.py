class Node:
    def __init__(self, key, parent=None, left=-1, right=-1):
        self.key = key
        self.parent = None
        self.left = -1
        self.right = -1

class BinaryTree:
    def __init__(self):
        self.root = None
        self.len = 0

    def addByStr(self, parent_key, key, child):
        new_elem = Node(key)
        root_elem = self.root
        if root_elem is None:
            self.root = new_elem
            self.len += 1
            print(new_elem.key)
        else:
            old_elem = self.find(parent_key)
            if child == 'left':
                old_elem.left = new_elem
                new_elem.parent = old_elem
                self.len += 1
                print(new_elem.key)
            else:
                old_elem.right = new_elem
                new_elem.parent = old_elem
                self.len += 1
                print(new_elem.key)

    def find(self, key, Node=None):
        if Node is None:
            Node = self.root
        while key != Node.key:
            if Node.left == -1 and Node.right == -1:
                return -1
            elif Node.left != -1 and Node.right != -1:
                elem = self.find(key, Node.left)
                if elem != -1:
                    return elem
                elem = self.find(key, Node.right)
                if elem != -1:
                    return elem
            elif Node.left == -1 and Node.right != -1:
                elem = self.find(key, Node.right)
                if elem != -1:
                    return elem
            elif Node.left != -1 and Node.right == -1:
                elem = self.find(key, Node.left)
                if elem != -1:
                    return elem
            return -1
        else:
            elem = Node
            return elem

    def inOrder(self):
        Node = self.root
        nodes = 0
        while nodes < self.len:
            if Node.left != -1:
                Node = Node.left
            else:
                print(Node.key, end=' ')
                Node = Node.parent
                print(Node.key, end=' ')
                
def main():
    n = int(input())
    A = []
    for i in range(n):
        *a, = map(int, input().split())
        A.append(a)
    Tree = BinaryTree()
    Tree.addByStr(A[0][0], A[0][0], 'left')
    MakeTree(Tree, A, 0)


def MakeTree(Tree, A, i):

        if A[i][1] != -1:
            child = 'left'
            j = i
            Tree.addByStr(A[i][0], A[A[i][1]][0], child)
            i = A[i][1]
            MakeTree(Tree, A, i)
            i = j
        if A[i][2] != -1:
            child = 'right'
            Tree.addByStr(A[i][0], A[A[i][2]][0], child)
            i = A[i][2]
            MakeTree(Tree, A, i)
        return
main()
