import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest_pair(points):
    min_dist = float('inf')
    n = len(points)
    if n < 2:
        return min_dist
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def closest_pair_recursive(points_sorted_by_x):
    n = len(points_sorted_by_x)

    if n <= 3:
        return brute_force_closest_pair(points_sorted_by_x)

    mid = n // 2
    mid_point = points_sorted_by_x[mid]

    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

    d1 = closest_pair_recursive(left_half)
    d2 = closest_pair_recursive(right_half)
    delta = min(d1, d2)

    strip = []
    for p in points_sorted_by_x:
        if abs(p[0] - mid_point[0]) < delta:
            strip.append(p)

    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= delta:
                break
            dist = euclidean_distance(strip[i], strip[j])
            if dist < delta:
                delta = dist
    return delta

def shortest_distance_in_plane(points):
    if len(points) < 2:
        return 0.0

    points_sorted_by_x = sorted(points, key=lambda p: p[0])

    return closest_pair_recursive(points_sorted_by_x)