import heapq
def processors(A, n):
    Heap = [[0, i] for i in range(n)]
    heapq.heapify(Heap)
    i = 0
    while i < len(A):
        min = heapq.heappop(Heap)
        print(' '.join(str(min[i]) for i in range(len(min) - 1, -1, -1)))
        min[0] += A[i]
        heapq.heappush(Heap, min)
        i += 1

def main():
    n, m = map(int, input().split())
    *A, = map(int, input().split())
    processors(A, n)

main()
