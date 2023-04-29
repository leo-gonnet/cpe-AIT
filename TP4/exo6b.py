import matplotlib.pyplot as plt

def is_left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def quick_hull(points):
    if len(points) < 3:
        return points
    points = sorted(points, key=lambda x: x[0])
    leftmost = points[0]
    rightmost = points[-1]
    hull = [leftmost, rightmost]
    points.remove(leftmost)
    points.remove(rightmost)
    left_points = []
    right_points = []
    for point in points:
        if is_left(leftmost, rightmost, point):
            left_points.append(point)
        else:
            right_points.append(point)
    hull.extend(quick_hull(left_points))
    hull.extend(quick_hull(right_points))
    return hull

points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

n = len(points)
res = quick_hull(points)

print(points)


fig = plt.figure()
plt.scatter(*zip(*points))

print(res)
plt.scatter(*zip(*res), color='red')

plt.show()