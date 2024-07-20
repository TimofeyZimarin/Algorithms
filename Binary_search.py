import sys
from math import floor

def Binary_search(a:list, i: int) -> int:
    l = 0
    r = len(a) - 1
    while l <= r:
        m = floor(l + (r - l) / 2)
        if a[m] == i:
            return m + 1
        elif a[m] > i:
            r = m - 1
        else:
            l = m + 1

    return -1

def main():
    reader = sys.stdin
    reader = [int(i) for i in next(reader).split()]
    n, *a = reader
    reader = sys.stdin
    reader = [int(i) for i in next(reader).split()]
    k, *b = reader
    for i in range(k):
        print(Binary_search(a, b[i]), end=' ')



if __name__ =='__main__':
    main()