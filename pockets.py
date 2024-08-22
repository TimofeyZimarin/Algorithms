import sys
def pockets(data, size):
    stek = size
    time = 0
    i = 0
    while i < len(data):
        if stek == size:
            stek -= 1
            time += data[i][1]
            j = 1
            while time > data[j][0] and stek > 0:
                j += 1





def main():
    reader = sys.stdin
    data = []
    size, n = map(int, next(reader).split())
    for i in range(n):
        a, d = map(int, next(reader).split())
        data.append((a, d))
    print(size, n)
    print(data)

main()