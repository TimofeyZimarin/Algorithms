def MakeSet(parent, i):
    parent[i] = i


def Find(parent, i):
    if parent[i] == -100:
        return -100
    if i != parent[i]:
        parent[i] = Find(parent, parent[i])
    return parent[i]


def Union(parent, rank, i, j):
    i_id = Find(parent, i)
    j_id = Find(parent, j)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = parent[i_id]

    else:
        parent[i_id] = parent[j_id]
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1


def main():
    n, e, d = map(int, input().split())
    E = []
    D = []
    flag = True
    parent = [-100 for i in range(n)]
    rank = [0 for i in range(n)]
    for i in range(e):
        l, r = map(int, input().split())
        E.append([l, r])
        MakeSet(parent, l - 1)
        MakeSet(parent, r - 1)
    for i in range(d):
        l, r = map(int, input().split())
        D.append([l, r])
    for i in range(e):
        Union(parent, rank, E[i][0] - 1, E[i][1] - 1)
    for i in range(d):
        l = Find(parent, D[i][0] - 1)
        r = Find(parent, D[i][1] - 1)
        # if D[i][0] == D[i][1]:
        #     flag = False
        if l == r and l != -100:
            flag = False

    print(int(flag))


main()
