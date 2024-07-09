def Haffmans_decode():

    k, l = map(int, input().split())
    S = {}
    for i in range(k):
        a, b = input().split(':')
        S[b[1:]] = a
    s = str(input())

    temp = ''
    output = ''
    i = 0
    # if len(s) == 1:
    #     print(S[s])
    # else:
    while i < len(s):
        if temp not in S:
            temp += s[i]
            i += 1
        elif temp in S:
            output += S[temp]
            temp = ''
    else:
        if temp in S:
            output += S[temp]



    return print(output)

Haffmans_decode()