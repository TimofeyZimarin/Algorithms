def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = [0, 1]
    for i in range(2, n + 1):
        fib[0], fib[1] = fib[1], fib[0] + fib[1]
    return fib[1]

def fib_digit(n):
    if n == 1:
        return 1
    fib = [0, 1]
    for i in range(2, n + 1):
        temp = (fib[0] + fib[1]) % 10
        fib[0], fib[1] = fib[1], temp
    return fib[-1]

def fib_mod(n, m):
    if n == 1:
        return m
    fib = [0, 1]
    ost = [0, 1]
    for i in range(2, n + 1):
        fib[0], fib[1] = fib[1], fib[0] + fib[1]
        ost.append(fib[-1] % m)
        if ost[-1] == 1 and ost [-2] == 0:
            return ost[n % (len(ost) - 2)]
    return fib[-1] % m


def main():
    n= int(input())
    print(fib(n))
    #print(fib(n))


if __name__ == "__main__":
    main()

