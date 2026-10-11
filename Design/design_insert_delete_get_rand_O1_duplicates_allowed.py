import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indeces = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.indeces[val].add(len(self.nums) - 1)

        if len(self.indeces[val]) == 1:
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val not in self.indeces:
            return False

        idx = self.indeces[val].pop()
        last_idx = len(self.nums) - 1
        last_val = self.nums[last_idx]

        self.indeces[last_val].add(idx)
        self.indeces[last_val].discard(last_idx)

        if len(self.indeces[val]) == 0:
            del self.indeces[val]

        self.nums[idx] = last_val
        self.nums.pop()

        return True
        

    def getRandom(self) -> int:
        if len(self.nums) == 0:
            return -1
        
        rand = random.randint(0, len(self.nums) - 1)
        return self.nums[rand]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()