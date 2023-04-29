from math import sqrt
import matplotlib.pyplot as plt


def distPointLine(p, q, r):
    sub = (q[1] - p[1]) ** 2 + (q[0] - p[0]) ** 2
    if sub == 0:
        return 0
    return abs((q[1] - p[1]) * r[0] - (q[0] - p[0]) * r[1] + q[0] * p[1] - q[1] * p[0]) / sqrt(sub)

def quickHull(points, p, q, n):
    if n == 0:
        return []

    max_dist = 0
    for i in range(n):
        dist = distPointLine(p, q, points[i])
        if dist > max_dist:
            max_dist = dist
            max_point = points[i]

    res = []
    res.extend(quickHull(points, p, max_point, n))
    res.append(max_point)
    res.extend(quickHull(points, max_point, q, n))

    return res



if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

    n = len(points)
    res = quickHull(points, points[0], points[1], n)

    print(points)


    fig = plt.figure()
    plt.scatter(*zip(*points))

    print(res)
    #plt.scatter(*zip(*res), color='red')

    plt.show()