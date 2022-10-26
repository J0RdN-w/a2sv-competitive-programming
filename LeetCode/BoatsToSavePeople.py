class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats, f, r = 0, 0, len(people) - 1
        while f <= r:
            if f == r or people[f] + people[r] <= limit:
                f += 1
            r -= 1
            boats += 1

        return boats
