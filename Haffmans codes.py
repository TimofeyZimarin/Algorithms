def Haffmans_codes(s):

    H = []
    S = {}
    for i in range(len(s)):
        F = s.count(s[i])
        if s[i] not in S:
            S[s[i]] = F
            H.append((s[i], F))

    H.sort(key=lambda x: x[1], reverse=True)

    i = 0
    tree = []
    while len(H) > 0:
        if len(H) == 1:
            last_1 = H.pop()
            tree.append(last_1)
        else:
            F = H[-1][1]
            F_1 = H[-2][1]
            name = H[-1][0] + H[-2][0]
            last_1 = H.pop()
            last_2 = H.pop()
            tree.append(last_1)
            tree.append(last_2)
            H.append((name, F + F_1, [last_2[0], last_1[0]]))
            H.sort(key=lambda x: x[1], reverse=True)


    return tree

def codes(tree, elem=-1, num='', S={}):


    while len(tree) > 0:
        knot = tree[elem]
        if len(knot) == 3:
            for i in knot[2]:
                j = 0
                while tree[j][0] != i:
                    j += 1
                if knot[2].index(i) == 0:
                    num += '0'
                    k = j
                    codes(tree, j, num, S)
                    j = k - 1
                    i = tree[j][0]

                else:
                    num += '1'
                    codes(tree, j, num, S)
                    j = k - 1
                    i = tree[j][0]
        elif len(knot) != 3:
            S[knot[0]] = num
            num = num[:-1]
            return num









    # return print(k, len(s_new)), [print(f'{i[0]}: {S[i[0]]}') for i in H_new], print(s_new)

codes(Haffmans_codes('accepted'))

Haffmans_codes(str(input()))

s = 'aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccddd'
