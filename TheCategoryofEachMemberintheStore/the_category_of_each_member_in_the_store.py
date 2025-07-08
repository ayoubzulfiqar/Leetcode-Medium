class StoreMember:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"StoreMember(name='{self.name}', category='{self.category}')"

class Store:
    def __init__(self):
        self.members = {}  # Stores members by name: {name: StoreMember_object}

    def add_member(self, name: str, category: str):
        """
        Adds a new member to the store or updates an existing member's category.
        """
        if name in self.members:
            # print(f"Warning: Member '{name}' already exists. Updating category to '{category}'.")
            pass # Suppress print for strict output
        self.members[name] = StoreMember(name, category)

    def get_member_category(self, name: str) -> str | None:
        """
        Retrieves the category of a specific member.
        Returns the category string if found, otherwise None.
        """
        member = self.members.get(name)
        if member:
            return member.category
        return None

    def list_all_members(self) -> list[StoreMember]:
        """
        Returns a list of all StoreMember objects currently in the store.
        """
        return list(self.members.values())

    def list_members_by_category(self) -> dict[str, list[str]]:
        """
        Organizes and returns members grouped by their categories.
        Returns a dictionary where keys are categories (str) and values are lists of member names (str).
        """
        categories_map = {}
        for member_name, member_obj in self.members.items():
            if member_obj.category not in categories_map:
                categories_map[member_obj.category] = []
            categories_map[member_obj.category].append(member_name)
        return categories_map

if __name__ == "__main__":
    # Create a new store instance
    my_store = Store()

    # Add various members with their respective categories
    my_store.add_member("Alice", "Premium")
    my_store.add_member("Bob", "Standard")
    my_store.add_member("Charlie", "VIP")
    my_store.add_member("David", "Standard")
    my_store.add_member("Eve", "Premium")
    my_store.add_member("Frank", "VIP")

    # Demonstrate updating a member's category
    my_store.add_member("Bob", "VIP") # Bob's category changes from Standard to VIP

    # Retrieve and print categories for specific members
    print(f"Alice's category: {my_store.get_member_category('Alice')}")
    print(f"Bob's category: {my_store.get_member_category('Bob')}")
    print(f"Zoe's category: {my_store.get_member_category('Zoe')}") # Member not found

    # List all members and their categories
    print("\nAll members in the store:")
    for member in my_store.list_all_members():
        print(f"- {member.name} ({member.category})")

    # Group members by category and print the result
    print("\nMembers grouped by category:")
    members_by_cat = my_store.list_members_by_category()
    for category, member_names in members_by_cat.items():
        print(f"Category '{category}': {', '.join(member_names)}")