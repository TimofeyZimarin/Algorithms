class MinHeap():

    def __init__(self):
        self.heap = []

    def Insert(self, priority):
        self.heap.append(priority)
        flag = True
        i = len(self.heap) - 1
        while flag:
            if self.heap[i][1] < self.heap[(i - 1) // 2][1] and ((i - 1) // 2) >= 0:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
                i = (i - 1) // 2
            elif self.heap[i][1] == self.heap[(i - 1) // 2][1] and ((i - 1) // 2) >= 0 and self.heap[i][0] < self.heap[(i - 1) // 2][0]:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
                i = (i - 1) // 2
            else:
                flag = False

        return self.heap

    def ExtractMin(self):
        if len(self.heap) == 1:
            minimum = self.heap.pop()
        else:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            minimum = self.heap[-1]
            self.heap = self.heap[:-1]
            flag = True
            i = 0
            while flag:
                if (i * 2 + 2) <= len(self.heap) - 1:
                    if self.heap[i * 2 + 1][1] > self.heap[i * 2 + 2][1]:
                        if self.heap[i * 2 + 2][1] < self.heap[i][1] or self.heap[i * 2 + 2][0] < self.heap[i][0]:
                            self.heap[i], self.heap[i * 2 + 2] = self.heap[i * 2 + 2], self.heap[i]
                            i = i * 2 + 2
                    elif self.heap[i * 2 + 1][1] < self.heap[i * 2 + 2][1]:
                        if self.heap[i * 2 + 1][1] < self.heap[i][1] or self.heap[i * 2 + 1][0] < self.heap[i][0]:
                            self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                            i = i * 2 + 1
                    elif self.heap[i * 2 + 1][1] == self.heap[i * 2 + 2][1] and self.heap[i * 2 + 1][1] < self.heap[i][1]:
                        if self.heap[i * 2 + 1][0] < self.heap[i * 2 + 2][0]:
                            self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                            i = i * 2 + 1
                        else:
                            self.heap[i], self.heap[i * 2 + 2] = self.heap[i * 2 + 2], self.heap[i]
                            i = i * 2 + 2
                    elif self.heap[i * 2 + 1][1] == self.heap[i * 2 + 2][1] and self.heap[i * 2 + 2][1] == self.heap[i][1]:
                        if self.heap[i * 2 + 2][0] < self.heap[i * 2 + 1][0]:
                            self.heap[i], self.heap[i * 2 + 2] = self.heap[i * 2 + 2], self.heap[i]
                            i = i * 2 + 2
                        else:
                            self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                            i = i * 2 + 1
                    else:
                        flag = False
                elif (i * 2 + 1) <= len(self.heap) - 1:
                    if self.heap[i * 2 + 1][1] < self.heap[i][1]:
                        self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                        i = i * 2 + 1
                    elif self.heap[i * 2 + 1][1] == self.heap[i][1] and self.heap[i * 2 + 1][0] < self.heap[i][0]:
                        self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                        i = i * 2 + 1
                    else:
                        flag = False
                else:
                    flag = False

        return minimum

    def print(self):
        print(self.heap)

def processors(A, n):
    Heap = MinHeap()
    P = [[i, 0] for i in range(n)]
    for i in range(len(P)):
        Heap.Insert(P[i])
    i = 0
    while i < len(A):
        # Heap.print()
        min = Heap.ExtractMin()
        # Heap.print()
        print(' '.join(str(i) for i in min))
        min[1] += A[i]
        # Heap.print()
        Heap.Insert(min)
        # Heap.print()
        i += 1

def main():
    n, m = map(int, input().split())
    *A, = map(int, input().split())
    processors(A, n)

main()
