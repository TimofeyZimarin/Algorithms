
def SiftDown(A, i, f):
    while i < f + 1:
        if i * 2 + 1 < f + 1 and i * 2 + 2 < f + 1:
            if A[i * 2 + 1] <= A[i * 2 + 2]:
                if A[i] < A[i * 2 + 2]:
                    A[i], A[i * 2 + 2] = A[i * 2 + 2], A[i]
                    i = i * 2 + 2
                else:
                    return A
            elif A[i * 2 + 2] < A[i * 2 + 1]:
                if A[i] < A[i * 2 + 1]:
                    A[i], A[i * 2 + 1] = A[i * 2 + 1], A[i]
                    i = i * 2 + 1
                else:
                    return A
            else:
                return A
        elif i * 2 + 1 < f + 1 and i * 2 + 2 == f + 1:
            if A[i] < A[i * 2 + 1]:
                A[i], A[i * 2 + 1] = A[i * 2 + 1], A[i]
                i = i * 2 + 1
            else:
                return A
        else:
            return A

def BuildMaxHeap(A):
    for i in range(((len(A) - 1) // 2), -1, -1):
        SiftDown(A, i, len(A) - 1)
    return A


def HeapSort(A):
    A = BuildMaxHeap(A)
    size = len(A) - 1
    for i in range(len(A) - 1, 0, -1):
        A[size], A[0] = A[0], A[size]
        size = size - 1
        SiftDown(A, 0, size)
    return A