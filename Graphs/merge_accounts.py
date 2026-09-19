class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        id_counter = 0
        email_to_id = {}
        email_to_name = {}

        # Bind each account to a unique int id so we can connect to DSU parent
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    id_counter += 1
                email_to_name[email] = name

        parent = [x for x in range(len(email_to_id))]
        rank = [1] * len(email_to_id)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        # Unionize all the emails that belong to the same person
        for account in accounts:
            first_email_id = email_to_id[account[1]]
            for email in account[2:]:
                second_email_id = email_to_id[email]
                union(first_email_id, second_email_id)


        # Actually create the bukets
        root_to_email = defaultdict(list)
        for email, email_id in email_to_id.items():
            root = find(email_id)
            root_to_email[root].append(email)
        
        #Package it
        res = []
        for emails in root_to_email.values():
            name = email_to_name[emails[0]]
            res.append([name] + sorted(emails))

        return res

        
