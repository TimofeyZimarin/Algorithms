class Heap():

    def __init__(self, heap=[]):
        self.heap = heap

    def read(self):
        s = str(input())
        command = s.split()
        return command

    def Insert(self, heap, priority):
        heap.append(priority)
        flag = True
        i = len(heap) - 1
        while flag:
            if heap[i] > heap[(i - 1) // 2] and ((i - 1) // 2) >= 0:
                heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
                i = (i - 1) // 2
            else:
                flag = False

        return heap

    def ExtractMax(self, heap):
        if len(heap) == 1:
            maximum = heap.pop()
        else:
            heap[0], heap[-1] = heap[-1], heap[0]
            maximum = heap.pop()
            flag = True
            i = 0
            while flag:
                if (i * 2 + 2) <= len(heap) - 1:
                    if heap[i * 2 + 1] >= heap[i * 2 + 2] and heap[i * 2 + 1] > heap[i]:
                        heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
                        i = i * 2 + 1
                    elif heap[i * 2 + 1] <= heap[i * 2 + 2] and heap[i * 2 + 2] > heap[i]:
                        heap[i], heap[i * 2 + 2] = heap[i * 2 + 2], heap[i]
                        i = i * 2 + 2
                    else:
                        flag = False
                elif (i * 2 + 1) <= len(heap) - 1:
                    if heap[i * 2 + 1] > heap[i]:
                        heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
                        i = i * 2 + 1
                    else:
                        flag = False
                else:
                    flag = False

        return print(maximum)
    def main(self):
        n = int(input())
        for i in range(n):
            data = Heap.read(self)
            if len(data) == 2:
                command, priority = data[0], int(data[-1])
                Heap.Insert(self, self.heap, priority)
            else:
                Heap.ExtractMax(self, self.heap)

        return self.heap
Heap().main()