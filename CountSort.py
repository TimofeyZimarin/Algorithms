
def CountSort(A):
    B = [0] * 10
    for i in A:
        B[i - 1] += 1

    for i in range(1, len(B)):
        B[i] += B[i - 1]

    A_1 = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        A_1[B[A[i] - 1] - 1] = A[i]
        B[A[i] - 1] -= 1
    return A_1