def SiftDown(A, i, f, m, ind):
    while i < f:
        if i * 2 + 1 < f and i * 2 + 2 < f:
            if A[i * 2 + 1] <= A[i * 2 + 2]:
                if A[i] > A[i * 2 + 1]:
                    A[i], A[i * 2 + 1] = A[i * 2 + 1], A[i]
                    ind.append([i, i * 2 + 1])
                    i = i * 2 + 1
                    m += 1
                else:
                    return A, m, ind
            elif A[i * 2 + 2] < A[i * 2 + 1]:
                if A[i] > A[i * 2 + 2]:
                    A[i], A[i * 2 + 2] = A[i * 2 + 2], A[i]
                    ind.append([i, i * 2 + 2])
                    i = i * 2 + 2
                    m += 1
                else:
                    return A, m, ind
            else:
                return A, m, ind
        elif i * 2 + 1 < f and i * 2 + 2 == f:
            if A[i] > A[i * 2 + 1]:
                A[i], A[i * 2 + 1] = A[i * 2 + 1], A[i]
                ind.append([i, i * 2 + 1])
                i = i * 2 + 1
                m += 1
            else:
                return A, m, ind
        else:
            return A, m, ind

def BuildMinHeap(A):
    m = 0
    ind = []
    for i in range(((len(A) - 1) // 2), -1, -1):
        A, m, ind = SiftDown(A, i, len(A), m, ind)
    return A, m, ind

A = [1, 2, 3, 4, 5]

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    A, m, ind =BuildMinHeap(A)
    print(m)
    for i in range(len(ind)):
        print(f"{ind[i][0]} {ind[i][1]}")

if __name__ == "__main__":
    main()