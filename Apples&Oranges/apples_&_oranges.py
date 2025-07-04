def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    for distance in apples:
        landing_position = a + distance
        if s <= landing_position <= t:
            apple_count += 1
    
    orange_count = 0
    for distance in oranges:
        landing_position = b + distance
        if s <= landing_position <= t:
            orange_count += 1
            
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples_str = input().rstrip().split()
    apples = list(map(int, apples_str))

    oranges_str = input().rstrip().split()
    oranges = list(map(int, oranges_str))

    countApplesAndOranges(s, t, a, b, apples, oranges)