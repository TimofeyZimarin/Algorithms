import sys

def LIDBottomUp(A:list):

    D = [1]

    for i in range(1, len(A)):
        D.append(1)
        for j in range(i):
            if A[i] != 0:
                if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                    D[i] += 1
    ans = 0
    for i in range(len(D)):
        ans = max(ans, D[i])
    return ans


def LNISBottomUp(A: list):
    D = [1]
    if len(A) == 1:
        ans = A[-1]
        ind = 0
    else:
        ans = 1
        ind = len(A) - 1


    for i in range(1, len(A)):
        D.append(1)
        for j in range(i):
            if A[i] <= A[j] and D[j] + 1 > D[i]:
                D[i] += 1
                if D[i] > ans:
                    ans = D[i]
                    ind = i

    L = [ind + 1] * ans
    j = len(L) - 2
    curr = ind
    for i in range(ind - 1, -1, -1):
        if D[i] == D[curr] - 1 and A[i] >= A[curr]:
            L[j] = i + 1
            curr = i
            j -= 1
    L = ' '.join(str(i) for i in L)
    return ans, L

def main():
    n = int(next(sys.stdin))
    reader = (map(int, line.split()) for line in sys.stdin)
    *A, = next(reader)
    A = LNISBottomUp(A)
    print(A[0], A[1], sep='\n')

if __name__ == '__main__':
    main()