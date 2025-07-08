def filter_banned_accounts(accounts, banned_accounts):
    banned_set = set(banned_accounts)
    filtered_accounts = []
    for account in accounts:
        if account not in banned_set:
            filtered_accounts.append(account)
    return filtered_accounts

if __name__ == "__main__":
    accounts1 = ["alice", "bob", "alice", "charlie", "david"]
    banned1 = ["alice", "eve"]
    result1 = filter_banned_accounts(accounts1, banned1)

    accounts2 = ["user1", "user2", "user3"]
    banned2 = ["user1", "user3"]
    result2 = filter_banned_accounts(accounts2, banned2)

    accounts3 = ["admin", "guest"]
    banned3 = []
    result3 = filter_banned_accounts(accounts3, banned3)

    accounts4 = []
    banned4 = ["banned_user"]
    result4 = filter_banned_accounts(accounts4, banned4)