def Numbers():
    n = int(input())
    nums = []
    sum = 0
    i = 1
    while n - sum:
        if n - sum >= i:
            nums.append(i)
            sum += i
            i += 1
        elif n - sum < i:
            sum -= i - 1
            nums.pop()
            nums.append(n - sum)
            sum = n

    return print(len(nums)), [print(i, end=' ') for i in nums]
Numbers()