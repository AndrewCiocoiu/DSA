from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()

            if d < r:
                dire.append(d + len(senate))
            else:
                radiant.append(r + len(senate))

        return "Radiant" if radiant else "Dire"
