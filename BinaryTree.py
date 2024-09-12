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







import sys, time
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = -1
        self.right = -1

class BinaryTree:
    def __init__(self):
        self.root = None
        self.last = None
        self.len = 0
        self.parents_queue = []

    def addByStr(self, parent_key, key, child):
        new_elem = Node(key)
        if self.root is None:
            self.root =new_elem
        if parent_key == self.last.key:
            old_elem = self.last
        else:
            old_elem = self.find(parent_key)
        if child == 'left':
            old_elem.left = new_elem
            new_elem.parent = old_elem
            self.last = new_elem
        else:
            old_elem.right = new_elem
            new_elem.parent = old_elem
            self.last = new_elem

    def addByList(self, A, i):
        if self.root is None:
            new_elem = Node(A[0][0])
            self.root = new_elem
            self.parents_queue.append(new_elem)

        if A[i][1] != -1:
            j = i
            new_elem = Node(A[A[i][1]][0])
            old_elem = self.parents_queue[-1]
            old_elem.left = new_elem
            new_elem.parent = old_elem
            self.parents_queue.append(new_elem)
            i = A[i][1]
            self.addByList(A, i)
            i = j
        else:
            self.parents_queue.pop()
        if A[i][2] != -1:
            j = i
            new_elem = Node(A[A[i][2]][0])
            old_elem = self.parents_queue[-1]
            old_elem.right = new_elem
            new_elem.parent = old_elem
            self.parents_queue.append(new_elem)
            i = A[i][2]
            self.addByList(A, i)
            i = j
        else:
            if A[i][1] != -1:
                self.parents_queue.pop()
            return
        if len(self.parents_queue) != 0:
            self.parents_queue.pop()
        return

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

    def InOrder(self, Node=None, result=[]):
        if Node is None:
            Node = self.root
        if Node.left != -1 and Node.right != -1:
            self.InOrder(Node.left, result)
            result.append(Node.key)
            self.InOrder(Node.right, result)
        elif Node.left != -1 and Node.right == -1:
            self.InOrder(Node.left, result)
            result.append(Node.key)
        elif Node.left == -1 and Node.right != -1:
            result.append(Node.key)
            self.InOrder(Node.right, result)
        elif Node.left == -1 and Node.right == -1:
            result.append(Node.key)
            return
        return result

    def PreOrder(self, Node=None, result=[]):
        if Node is None:
            Node = self.root
        if Node.left != -1 and Node.right != -1:
            result.append(Node.key)
            self.PreOrder(Node.left, result)
            self.PreOrder(Node.right, result)
        elif Node.left != -1 and Node.right == -1:
            result.append(Node.key)
            self.PreOrder(Node.left, result)
        elif Node.left == -1 and Node.right != -1:
            result.append(Node.key)
            self.PreOrder(Node.right, result)
        elif Node.left == -1 and Node.right == -1:
            result.append(Node.key)
            return
        return result

    def PostOrder(self, Node=None, result=[]):
        if Node is None:
            Node = self.root
        if Node.left != -1 and Node.right != -1:
            self.PostOrder(Node.left, result)
            self.PostOrder(Node.right, result)
            result.append(Node.key)
        elif Node.left != -1 and Node.right == -1:
            self.PostOrder(Node.left, result)
            result.append(Node.key)
        elif Node.left == -1 and Node.right != -1:
            self.PostOrder(Node.right, result)
            result.append(Node.key)
        elif Node.left == -1 and Node.right == -1:
            result.append(Node.key)
            return
        return result

def main():
    # reader = sys.stdin
    # n = int(next(reader))
    n = int(input())
    A = []
    for i in range(n):
        # *a, = map(int, next(reader).split())
        *a, = map(int, input().split())
        A.append(a)
    Tree = BinaryTree()
    Tree.addByList(A, 0)
    # MakeTree(Tree, A, 0)

    In = Tree.InOrder()
    s_in = ' '.join(str(i) for i in In)
    print(s_in)
    Pre = Tree.PreOrder()
    s_pre = ' '.join(str(i) for i in Pre)
    print(s_pre)
    Post = Tree.PostOrder()
    s_post = ' '.join(str(i) for i in Post)
    print(s_post)

# def MakeTree(Tree, A, i):
#
#         if A[i][1] != -1:
#             child = 'left'
#             j = i
#             Tree.addByStr(A[i][0], A[A[i][1]][0], child)
#             i = A[i][1]
#             MakeTree(Tree, A, i)
#             i = j
#         if A[i][2] != -1:
#             child = 'right'
#             Tree.addByStr(A[i][0], A[A[i][2]][0], child)
#             i = A[i][2]
#             MakeTree(Tree, A, i)
#         return
main()
