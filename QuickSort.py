import sys
import time
from math import floor

def Binary_search(a:list, i:int, s:str):
    l = 0
    r = len(a) - 1
    if s == 'l' and i < a[0]:
        return 0
    elif s == 'r' and i > a[-1]:
        return len(a)
    elif s == 'r' and i <= a[0]:
        return 0
    elif s == 'l' and i >= a[-1]:
        return len(a)
    ind = 0
    if s == 'l':
        while l <= r:
            m = floor(l + (r - l) / 2)
            if a[m] <= i:
                ind = m
                l = m + 1
            elif a[m] > i:
                r = m - 1
        return ind + 1
    elif s == 'r':
        while l <= r:
            m = floor(l + (r - l) / 2)
            if a[m] < i:
                ind = m
                l = m + 1
            elif a[m] >= i:
                r = m - 1
        return ind + 1



def partition(A:list, l, r):

    left, right, middle = A[l], A[r - 1], A[(r + l) // 2]
    if right >= left and right <= middle or right <= left and right >= middle:
        A[l], A[r - 1] = A[r - 1], A[l]
    elif middle >= left and middle <= right or middle <= left and middle >= right:
        A[l], A[(r + l) // 2] = A[(r +  l) // 2], A[l]
    x = A[l]
    j = l
    k = 0
    for i in range(l + 1, r):
        if x > A[i]:
            j += 1
            if i != j + k:
                A[j], A[j + k] = A[j + k], A[j]
                A[j], A[i] = A[i], A[j]
            else:
                A[j], A[i] = A[i], A[j]
        elif x == A[i]:
            k += 1
            A[j + k], A[i] = A[i], A[j + k]
    A[l], A[j] = A[j], A[l]

    return j, j + k






def QuickSort(A:list, l, r) -> list:

    while l < r:
        m_l, m_r = partition(A, l, r)
        QuickSort(A, l, m_l)
        l = m_r + 1

    return A

def main():
    reader = sys.stdin
    n, m = map(int, next(reader).split())
    L = []
    R = []
    for i in range(n):
        reader = sys.stdin
        a, b = map(int, next(reader).split())
        L.append(a)
        R.append(b)

    reader = sys.stdin
    *points, = map(int, next(reader).split())
    L_sorted = QuickSort(L, 0, len(L))
    R_sorted = QuickSort(R, 0, len(R))


    m = []
    for j in points:
        x = Binary_search(L_sorted, j, 'l')
        y = Binary_search(R_sorted, j, 'r')
        m.append(x - y)

    return ' '.join(str(i) for i in m)


if __name__ == '__main__':
    print(main())