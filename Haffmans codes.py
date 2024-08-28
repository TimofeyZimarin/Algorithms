import sys
def Haffmans_codes():

    s = str(input())
    H = []
    S = {}
    for i in range(len(s)):
        F = s.count(s[i])
        if s[i] not in S:
            S[s[i]] = F
            H.append((s[i], F))

    H.sort(key=lambda x: x[1], reverse=True)
    print(H)


    i = 0
    H_1 = []
    while len(H) > 1:
        F = H[-1][1]
        F_1 = H[-2][1]
        name = H[-1][0] + H[-2][0]
        last_1 = H.pop()
        last_2 = H.pop()
        H_1.append(last_1)
        H_1.append(last_2)
        H.append((name, F + F_1))
        H.sort(key=lambda x: x[1], reverse=True)


    H = H_1
    i = 0
    j = 0
    k = 0
    key = ''
    while i < len(H):
        if j == 0 and k % 2 == 0:
            key += '1'
            j += 1
        elif j == 0 and k % 2 != 0:
            key += '0'
            j += 1
        elif H[k][0] not in H[j][0]:
            j += 1
        elif H[k][0] in H[j][0] and j != len(H) - 1:
            if H[k][0][0] == H[j][0][0] and len(H[k][0]) != len(H[j][0]):
                key += '0'
            else:
                key += '1'
            k = j
            j += 1
        elif H[k][0] in H[j][0] and j == len(H) - 1:
            key += '0'
            S[H[i][0]] = key
            print(S)
            key = ''
            i += 1
            k = i
            j = 0
        elif H[k][0] in H[j][0] and j == len(H) - 2:
            key += '1'
            S[H[i][0]] = key
            print(S)
            key = ''
            i += 1
            k = i
            j = 0

    print(S)

    # for k in range(len(H) + 1, 2 * len(H) - 1):
    #     F = H[0 + i][1]
    #     F_1 = H[1 + i][1]
    #     print(H)
    #     H.insert(i + 2, (k, F + F_1))
    #     H.sort(key=lambda x: x[1])
    #     i += 2

    H_new = []
    H.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(H)):
        if H[i][0] in S:
            H_new.append(H[i])



















    # key = ''
    # j = 0
    # i = 0
    # while i < len(H_new) and len(H_new) != 1:
    #     if H_new[j][1] == H_new[i][1] and H_new[j][0] == H_new[i][0] and j < len(H_new) - 1:
    #         key += '0'
    #         S[H_new[j][0]] = key
    #         i = 0
    #         j += 1
    #         key = ''
    #     elif H_new[j][1] <= H_new[i][1] and H_new[j][0] != H_new[i][0]:
    #         key += '1'
    #         i += 1
    #     elif H_new[j][0] == H_new[i][0] and j == len(H_new) - 1:
    #         S[H_new[j][0]] = key
    #         i = len(H_new)
    #         key = ''
    # if len(H_new) == 1:
    #     S[H_new[0][0]] = '0'
    #
    # k = len(H_new)
    # bits = 0
    # s_new = ''
    # for i in range(len(s)):
    #     s_new += S[s[i]]
    #     # bits += len(S[H_new[i][0]])

    return print(k, len(s_new)), [print(f'{i[0]}: {S[i[0]]}') for i in H_new], print(s_new)

Haffmans_codes()

    # j = 0
    # i = 0
    # key = '0'
    #
    # while i < len(H) and j < len(H):
    #     if H[j][0] not in S:
    #         j += 1
    #     elif H[j][0] in S and H[j][1] < H[i][1]:
    #         key += '1'
    #         i += 1
    #     elif H[j][0] in S and H[j][1] == H[i][1] and j != len(H) - 1:
    #         key = key[:-1]
    #         key += '0'
    #         S[H[j][0]] = key
    #         key = key[:-1]
    #         j += 1
    #     elif H[j][0] in S and H[j][1] == H[i][1] and j == len(H) - 1:
    #         S[H[j][0]] = key
    #         j += 1
    # return print(H, S)

Haffmans_codes()

s = 'aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccddd' - 'aaaa'