def count_trusted_contacts(customer_contacts, trusted_individuals):
    """
    Counts the number of trusted contacts a customer has from a given list of contacts.

    Args:
        customer_contacts (list): A list of strings, representing the names of the customer's contacts.
        trusted_individuals (list): A list of strings, representing the names of individuals
                                    who are considered trusted.

    Returns:
        int: The total count of contacts from customer_contacts that are also present
             in trusted_individuals.
    """
    trusted_set = set(trusted_individuals)
    trusted_contact_count = 0

    for contact in customer_contacts:
        if contact in trusted_set:
            trusted_contact_count += 1

    return trusted_contact_count

if __name__ == '__main__':
    # Example Usage:
    customer_contacts_1 = ["Alice", "Bob", "Charlie", "David"]
    trusted_individuals_1 = ["Bob", "Eve", "Charlie", "Frank"]
    result_1 = count_trusted_contacts(customer_contacts_1, trusted_individuals_1)
    # Expected: Bob, Charlie -> 2
    print(f"Customer 1 trusted contacts: {result_1}")

    customer_contacts_2 = ["John", "Jane", "Doe"]
    trusted_individuals_2 = ["John", "Jane", "Peter"]
    result_2 = count_trusted_contacts(customer_contacts_2, trusted_individuals_2)
    # Expected: John, Jane -> 2
    print(f"Customer 2 trusted contacts: {result_2}")

    customer_contacts_3 = ["Alice", "Bob"]
    trusted_individuals_3 = ["Charlie", "David"]
    result_3 = count_trusted_contacts(customer_contacts_3, trusted_individuals_3)
    # Expected: 0
    print(f"Customer 3 trusted contacts: {result_3}")

    customer_contacts_4 = []
    trusted_individuals_4 = ["Alice", "Bob"]
    result_4 = count_trusted_contacts(customer_contacts_4, trusted_individuals_4)
    # Expected: 0
    print(f"Customer 4 trusted contacts: {result_4}")

    customer_contacts_5 = ["Alice", "Bob"]
    trusted_individuals_5 = []
    result_5 = count_trusted_contacts(customer_contacts_5, trusted_individuals_5)
    # Expected: 0
    print(f"Customer 5 trusted contacts: {result_5}")

    customer_contacts_6 = ["Alice", "Bob", "Alice"] # Duplicate in contacts list
    trusted_individuals_6 = ["Alice", "Charlie"]
    result_6 = count_trusted_contacts(customer_contacts_6, trusted_individuals_6)
    # Expected: Alice (first), Alice (second) -> 2
    print(f"Customer 6 trusted contacts: {result_6}")