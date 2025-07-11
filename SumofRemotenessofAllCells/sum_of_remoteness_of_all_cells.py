def solve(points):
    N = len(points)
    if N == 0:
        return 0

    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    x_coords.sort()
    y_coords.sort()

    total_remoteness = 0

    # Calculate sum for x-coordinates
    # The sum sum_{i}