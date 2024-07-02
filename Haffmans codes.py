class Haffmans_tree():

    s = str(input())
    def __init__(self, s=s):
        self.s = s

    def build_tree(self):

        H = []
        S = {}
        for i in range(len(self.s)):
            F = self.s.count(self.s[i])
            if self.s[i] not in S:
                S[self.s[i]] = F
                H.append((self.s[i], F))

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

    def codes(self, tree:list, elem=-1, num='', S={}, points=[], latters=[])-> tuple:

        while len(points) < len(tree):
            knot = tree[elem]
            flag = True
            if len(knot) == 3:
                for i in knot[2]:
                    if i not in points:
                        flag = False
                if flag == True:
                    points.append(knot[0])
                    return S, latters

            if len(knot) == 3:
                for i in knot[2]:
                    j = 0
                    while tree[j][0] != i:
                        j += 1
                    if knot[2].index(i) == 0:
                        num += '0'
                        Haffmans_tree.codes(self, tree, j, num, S)
                        num = num[:-1]
                    else:
                        num += '1'
                        Haffmans_tree.codes(self, tree, j, num, S)
                        num = num[:-1]
            elif len(knot) != 3:
                S[knot[0]] = num
                latters.append(knot[0])
                points.append(knot[0])
                return S, latters

    def print_tree(self, T:tuple):

        if len(T[0]) == 1:
            T[0][T[1][0]] = '0'
        k = len(T[1])
        bits = 0
        s_new = ''
        for i in range(len(self.s)):
            s_new += T[0][self.s[i]]
            # bits += len(S[H_new[i][0]])

        return print(k, len(s_new)), [print(f'{i}: {T[0][i]}') for i in T[1]], print(s_new)


Haffmans_tree().print_tree(Haffmans_tree().codes(Haffmans_tree().build_tree()))

