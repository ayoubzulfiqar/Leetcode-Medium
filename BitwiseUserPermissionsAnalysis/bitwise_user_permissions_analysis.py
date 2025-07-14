READ = 1 << 0
WRITE = 1 << 1
EXECUTE = 1 << 2
DELETE = 1 << 3
ADMIN = 1 << 4

PERMISSION_NAMES = {
    READ: "READ",
    WRITE: "WRITE",
    EXECUTE: "EXECUTE",
    DELETE: "DELETE",
    ADMIN: "ADMIN"
}

ALL_PERMISSION_MASKS = [READ, WRITE, EXECUTE, DELETE, ADMIN]

def has_permission(user_permissions: int, permission_to_check: int) -> bool:
    return (user_permissions & permission_to_check) == permission_to_check

def add_permission(user_permissions: int, permission_to_add: int) -> int:
    return user_permissions | permission_to_add

def remove_permission(user_permissions: int, permission_to_remove: int) -> int:
    return user_permissions & (~permission_to_remove)

def list_permissions(user_permissions: int) -> list[str]:
    granted_permissions = []
    for mask in ALL_PERMISSION_MASKS:
        if has_permission(user_permissions, mask):
            granted_permissions.append(PERMISSION_NAMES[mask])
    return granted_permissions

def get_common_permissions(permissions_set1: int, permissions_set2: int) -> int:
    return permissions_set1 & permissions_set2

def get_unique_permissions(permissions_set1: int, permissions_set2: int) -> int:
    return permissions_set1 & (~permissions_set2)

if __name__ == "__main__":
    user1_perms = READ | WRITE | ADMIN
    user2_perms = READ | EXECUTE | DELETE
    user3_perms = WRITE | DELETE

    print(f"User1 initial permissions: {list_permissions(user1_perms)}")
    print(f"User2 initial permissions: {list_permissions(user2_perms)}")
    print(f"User3 initial permissions: {list_permissions(user3_perms)}")
    print("-" * 30)

    print(f"Does User1 have READ? {has_permission(user1_perms, READ)}")
    print(f"Does User1 have EXECUTE? {has_permission(user1_perms, EXECUTE)}")
    print(f"Does User2 have WRITE? {has_permission(user2_perms, WRITE)}")
    print(f"Does User1 have READ and WRITE? {has_permission(user1_perms, READ | WRITE)}")
    print("-" * 30)

    print("Adding EXECUTE to User1...")
    user1_perms = add_permission(user1_perms, EXECUTE)
    print(f"User1 new permissions: {list_permissions(user1_perms)}")
    print(f"Does User1 now have EXECUTE? {has_permission(user1_perms, EXECUTE)}")
    print("-" * 30)

    print("Removing ADMIN from User1...")
    user1_perms = remove_permission(user1_perms, ADMIN)
    print(f"User1 new permissions: {list_permissions(user1_perms)}")
    print(f"Does User1 still have ADMIN? {has_permission(user1_perms, ADMIN)}")
    print("-" * 30)

    common_u1_u2 = get_common_permissions(user1_perms, user2_perms)
    print(f"Common permissions between User1 and User2: {list_permissions(common_u1_u2)}")

    common_u1_u3 = get_common_permissions(user1_perms, user3_perms)
    print(f"Common permissions between User1 and User3: {list_permissions(common_u1_u3)}")
    print("-" * 30)

    unique_u1_not_u2 = get_unique_permissions(user1_perms, user2_perms)
    print(f"Permissions User1 has that User2 does not: {list_permissions(unique_u1_not_u2)}")

    unique_u2_not_u1 = get_unique_permissions(user2_perms, user1_perms)
    print(f"Permissions User2 has that User1 does not: {list_permissions(unique_u2_not_u1)}")
    print("-" * 30)

    print("Adding WRITE and DELETE to User3...")
    user3_perms = add_permission(user3_perms, WRITE | DELETE)
    print(f"User3 new permissions: {list_permissions(user3_perms)}")
    print("-" * 30)

    print("Removing READ and EXECUTE from User2...")
    user2_perms = remove_permission(user2_perms, READ | EXECUTE)
    print(f"User2 new permissions: {list_permissions(user2_perms)}")
    print("-" * 30)