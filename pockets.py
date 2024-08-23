import sys

def pockets(data, size):
    stack = 0
    i = 0
    j = 0
    time_arr = []
    if len(data) == 0:
        return
    else:
        time = data[0][0]
    while i < len(data):
        flag = True
        if data[i][1] == 0:
            if stack == 0:
                time = data[i][0]
                time_arr.append(time)
                i += 1
                j += 1
            else:
                time_arr.append(time)
                stack -= 1
                i += 1
        else:
            if data[i][1] != -1 and data[i][0] >= time:
                time = data[i][0]
                time_arr.append(time)
                time += data[i][1]
            elif data[i][1] != -1 and data[i][0] < time:
                time_arr.append(time)
                time += data[i][1]
            else:
                time_arr.append(-1)
                flag = False

            while j < len(data) and time >= data[j][0] and flag:
                if time >= data[j][0] and stack < size:
                    stack += 1
                    j += 1
                elif time > data[j][0] and stack == size:
                    data[j][1] = -1
                    j += 1
                else:
                    break
            i += 1
            if stack != 0:
                stack -= 1
    return [print(i) for i in time_arr]

def main():
    reader = sys.stdin
    data = []
    size, n = map(int, next(reader).split())
    for i in range(n):
        a, d = map(int, next(reader).split())
        data.append([a, d])
    pockets(data, size)


main()
