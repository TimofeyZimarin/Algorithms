import heapq
from collections import Counter, namedtuple

class Node():

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def haffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _counter1,  left = heapq.heappop(h)
        freq2, _counter2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input()
    code = haffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

if __name__ == "__main__":
    main()