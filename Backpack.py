def Backpack():
    n, W = map(int, input().split())
    things = []
    for i in range(n):
        c, w = map(int, input().split())
        things.append((c, w, c / w))

    things.sort(key=lambda x:x[2], reverse=True)

    value = 0.0

    for i in range(len(things)):
        if things[i][1] < W:
            W = W - things[i][1]
            value += things[i][0]
        elif things[i][1] == W:
            W = 0
            value += things[i][0]
            break
        elif W != 0 and things[i][1] > W:
            part = W / things[i][1]
            W = 0
            value += things[i][0] * part
            break



    return print(f"{value:.3f}")

Backpack()