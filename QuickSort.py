import sys
import time

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
        x = 0
        y = 0
        for i in range(len(L_sorted)):
            if L_sorted[i] <= j:
                x += 1
            if R_sorted[i] < j:
                y += 1
        m.append(x - y)

    return ' '.join(str(i) for i in m)


if __name__ == '__main__':
    print(main())

# def sort(A, points):
#     for i in points:
#         flag = True
#         i = (len(A) - 1) // 2
#         while flag:
#             if A[i]

