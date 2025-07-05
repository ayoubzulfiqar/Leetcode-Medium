def count_calls_between_two_persons(calls, person1, person2):
    call_count = 0
    for caller, receiver, _timestamp in calls:
        if (caller == person1 and receiver == person2) or \
           (caller == person2 and receiver == person1):
            call_count += 1
    return call_count

if __name__ == "__main__":
    all_calls = [
        ("Alice", "Bob", 1678886400),
        ("Bob", "Alice", 1678886500),
        ("Charlie", "David", 1678886600),
        ("Alice", "Charlie", 1678886700),
        ("Bob", "Alice", 1678886800),
        ("David", "Charlie", 1678886900),
        ("Alice", "Bob", 1678887000),
        ("Eve", "Frank", 1678887100),
        ("Bob", "Charlie", 1678887200)
    ]

    p1_test1, p2_test1 = "Alice", "Bob"
    result1 = count_calls_between_two_persons(all_calls, p1_test1, p2_test1)

    p1_test2, p2_test2 = "Charlie", "David"
    result2 = count_calls_between_two_persons(all_calls, p1_test2, p2_test2)

    p1_test3, p2_test3 = "Alice", "Charlie"
    result3 = count_calls_between_two_persons(all_calls, p1_test3, p2_test3)

    p1_test4, p2_test4 = "Eve", "Bob"
    result4 = count_calls_between_two_persons(all_calls, p1_test4, p2_test4)