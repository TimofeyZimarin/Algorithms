import sys

def MergeSort(A, inv=0):
    l = 0
    r = len(A) - 1
    if l < r:
        m = (l + r) // 2
        Left = MergeSort(A[0:m + 1])
        Right = MergeSort(A[m + 1:])
        A_ret = Merge(Left[1], Right[1], Left[0] + Right[0])
        inv += A_ret[0]
        A = A_ret[1]
    return (inv, A)

def Merge(A_1, A_2, inv):
    i = 0
    j = 0
    A_sorted = []
    while i < len(A_1) or j < len(A_2):
        if i == len(A_1):
            A_sorted.append(A_2[j])
            j += 1
        elif j == len(A_2):
            A_sorted.append(A_1[i])
            i += 1
        elif A_1[i] <= A_2[j]:
            A_sorted.append(A_1[i])
            i += 1
        else:
            A_sorted.append(A_2[j])
            j += 1
            inv += len(A_1) - i

    return (inv, A_sorted)

def main():

    reader = sys.stdin
    n = int(next(reader))
    reader = sys.stdin
    A = [int(i) for i in next(reader).split()]
    A_sorted = MergeSort(A)
    print(A_sorted[0])


if __name__ == '__main__':
    main()