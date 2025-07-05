def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0

    for apple_dist in apples:
        landing_pos = a + apple_dist
        if s <= landing_pos <= t:
            apples_on_house += 1

    for orange_dist in oranges:
        landing_pos = b + orange_dist
        if s <= landing_pos <= t:
            oranges_on_house += 1

    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    st = list(map(int, input().rstrip().split()))
    s = st[0]
    t = st[1]

    ab = list(map(int, input().rstrip().split()))
    a = ab[0]
    b = ab[1]

    mn = list(map(int, input().rstrip().split()))
    m = mn[0]
    n = mn[1]

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)