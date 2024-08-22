def Segments():
    n = int(input())
    segments = []
    for i in range(n):
        a, b = map(int, input().split())
        segments.append((a, b))

    segments.sort(key=lambda x: x[1])

    i = 1
    points = []
    points.append(segments[0][1])
    while i < len(segments):
        if points[-1] >= segments[i][0]:
            i += 1
        else:
            points.append(segments[i][1])

    return print(len(points)), [print(i, end=' ') for i in points]

Segments()
