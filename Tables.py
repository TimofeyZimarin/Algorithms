import sys
sys.setrecursionlimit(100000)
def Find(parent, i):
    if i != parent[i]:
        parent[i] = Find(parent, parent[i])
    return parent[i]

def Union(parent, rank, sizes, i, j):
    i_id = Find(parent, i)
    j_id = Find(parent, j)
    if i_id == j_id:
        return sizes[i_id]
    if rank[i_id] > rank[j_id]:
        parent[j_id] = parent[i_id]
        sizes[i_id] += sizes[j_id]
        sizes[j_id] = 0
        return sizes[i_id]
    else:
        parent[i_id] = parent[j_id]
        sizes[j_id] += sizes[i_id]
        sizes[i_id] = 0
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1
        return sizes[j_id]
def adding(parent:list, rank, sizes, oper:list, max:int):
    i = 0
    while i < len(oper):
        a = Union(parent, rank, sizes, oper[i][0] - 1, oper[i][1] - 1)
        if a > max:
            max = a
        print(max)
        i += 1


def main():
    parent = []
    oper = []
    max = 0
    n, m = map(int, input().split())
    *sizes, = map(int, input().split())
    for i in range(m):
        *a, = map(int, input().split())
        oper.append(a)
    for i in range(n):
        parent.append(i)
        if max < sizes[i]:
            max = sizes[i]
    rank = [0 for _ in range(len(parent))]
    adding(parent, rank, sizes, oper, max)

main()
