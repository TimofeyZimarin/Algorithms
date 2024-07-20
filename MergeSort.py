import sys

def MergeSort(A):
    l = 0
    r = len(A) - 1
    if l < r:
        m = (l + r) // 2
        A = Merge(MergeSort(A[0:m + 1]), MergeSort(A[m + 1:]))
    return A

def Merge(A_1, A_2):
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

    return A_sorted

def main():

    reader = sys.stdin
    n = int(next(reader))
    reader = sys.stdin
    A = [int(i) for i in next(reader).split()]
    counter = 0

    A_sorted = MergeSort(A)

    return A_sorted

if __name__ == '__main__':
    print(main())