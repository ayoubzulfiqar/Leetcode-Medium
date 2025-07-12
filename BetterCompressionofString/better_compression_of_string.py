import collections

def solve():
    s = input()

    if not s:
        print("")
        return

    char_counts = collections.Counter(s)

    sorted_chars = sorted(char_counts.keys())

    compressed_parts = []
    for char in sorted_chars:
        compressed_parts.append(char)
        compressed_parts.append(str(char_counts[char]))

    print("".join(compressed_parts))

solve()