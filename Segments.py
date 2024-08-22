import sys


def pockets(data, size):
    stack = 0
    time = 0
    i = 0
    j = 0
    time_arr = []
    if len(data) == 0:
        return
    while i < len(data):
        if data[i][1] == 0:
            time_arr.append(time)
            i += 1
            j += 1
            if stack != 0:
                stack -= 1
            if i + 1 <= len(data) and stack == 0:
                time = data[i][0]
        else:
            if i == 0:
                time = data[i][0]
            if data[i][1] != -1:
                time_arr.append(time)
                time += data[i][1]
            else:
                time_arr.append(-1)
            while j < len(data) and time >= data[j][0]:
                if time >= data[j][0] and stack < size:
                    stack += 1
                    j += 1
                elif time > data[j][0] and stack == size:
                    data[j][1] = -1
                    j += 1
                elif time == data[j][0] and stack == size:
                    stack += 1
                else:
                    break

            i += 1
            stack -= 1




    return [print(i) for i in time_arr]


def main():
    reader = sys.stdin
    data = []
    # size, n = map(int, next(reader).split())
    # for i in range(n):
    #     a, d = map(int, next(reader).split())
    #     data.append([a, d])
    data = [[2, 9], [4, 8], [10, 9], [15, 2], [19, 1]]
    size = 2
    pockets(data, size)


main()
