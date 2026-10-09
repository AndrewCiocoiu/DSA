class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i = 0
        j = len(people) - 1
        count = 0

        current_limit = limit

        while i <= j:
            if people[j] <= current_limit:
                current_limit -= people[j]
                j -= 1

            if i <= j and people[i] <= current_limit:
                current_limit -= people[i]
                i += 1

            count += 1
            current_limit = limit

        return count