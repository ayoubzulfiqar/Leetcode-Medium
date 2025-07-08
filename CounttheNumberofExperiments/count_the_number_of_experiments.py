import sys

def solve():
    # Read the number of experiment IDs.
    # This value (N) determines how many IDs are expected on the next line.
    n = int(sys.stdin.readline())

    # Read the line containing space-separated experiment IDs.
    # .split() without arguments splits by any whitespace and returns a list of strings.
    experiment_ids_str = sys.stdin.readline().split()

    # Convert the list of string IDs to a list of integers.
    # This uses a list comprehension for concise and efficient conversion.
    experiment_ids = [int(x) for x in experiment_ids_str]

    # Use a set to automatically store only unique experiment IDs.
    # When elements are added to a set, duplicates are automatically discarded.
    unique_experiments = set(experiment_ids)

    # The number of unique experiments is the count of elements in the set.
    count = len(unique_experiments)

    # Print the final count to standard output.
    print(count)

# This block ensures that the solve() function is called only when the script is executed directly,
# not when it's imported as a module into another script.
if __name__ == '__main__':
    solve()