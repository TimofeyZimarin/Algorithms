from stack import stack


def window(data: list, m):
    a = stack()
    b = stack()
    maximum = []
    i = 0
    flag = True
    for i in range(m):
        a.push(data[i])
    i += 1
    while flag:
        for k in range(m):
            b.push(a.pop())
        k = 0
        while k < m and i <= len(data) and flag:
            first = b.max()
            b.pop()
            second = a.max()
            k += 1
            if first > second:
                maximum.append(first)
            else:
                maximum.append(second)
            if i < len(data):
                a.push(data[i])
                i += 1
            else:
                flag = False

    return ' '.join(str(i) for i in maximum)


def main():
    n = int(input())
    *data, = (map(int, input().split()))
    m = int(input())
    print(window(data, m))


if __name__ == '__main__':
    main()
