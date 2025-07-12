import math

def find_permutation_index(permutation_list):
    """
    Finds the 0-indexed lexicographical rank of a given permutation.

    Args:
        permutation_list: A list representing the permutation (e.g., [1, 3, 0, 2]).
                          Assumes elements are distinct and form a permutation
                          of some set of distinct values.

    Returns:
        The 0-indexed rank of the permutation.
    """
    n = len(permutation_list)
    if n == 0:
        return 0

    # Create a sorted list of available elements. This list will be
    # modified by removing elements as they are processed.
    # It represents the set of elements that are yet to be placed in the permutation.
    available_elements = sorted(list(permutation_list))

    index = 0

    # Iterate through the permutation from left to right
    for i in range(n):
        current_element = permutation_list[i]

        # Find the rank (0-indexed position) of the current_element
        # within the remaining available_elements.
        # This rank tells us how many elements *smaller* than the current_element
        # are still available to be placed at this position.
        rank = available_elements.index(current_element)

        # Add to the total index:
        # (number of smaller elements available at this position) * (permutations of remaining elements)
        # The number of remaining elements to be placed is (n - 1 - i).
        index += rank * math.factorial(n - 1 - i)

        # Remove the current_element from the available_elements list
        # as it has now been "used" in the permutation.
        available_elements.pop(rank)

    return index