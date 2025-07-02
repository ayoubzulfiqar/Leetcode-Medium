class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        parent = {}
        email_to_name = {}

        def find(email):
            if parent[email] == email:
                return email
            parent[email] = find(parent[email])
            return parent[email]

        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                parent[root1] = root2

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                other_email = account[i]
                union(first_email, other_email)

        merged_emails = {}
        for email in parent:
            root = find(email)
            if root not in merged_emails:
                merged_emails[root] = set()
            merged_emails[root].add(email)

        result = []
        for root_email, emails_set in merged_emails.items():
            name = email_to_name[root_email]
            sorted_emails = sorted(list(emails_set))
            result.append([name] + sorted_emails)

        return result