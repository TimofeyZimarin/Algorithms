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

def main():
    n = int(next(sys.stdin))
    reader = (map(int, line.split()) for line in sys.stdin)
    *A, = next(reader)
    print(LIDBottomUp(A))

if __name__ == '__main__':
    main()