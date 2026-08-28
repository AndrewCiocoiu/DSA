import random

class RandomizedSet:

    def __init__(self):
        self.my_set = {}
        self.my_arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.my_set:
            self.my_arr.append(val)
            self.my_set[val] = len(self.my_arr) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.my_set:
            return False
        idx = self.my_set[val]
        self.my_arr[idx] = self.my_arr[len(self.my_arr) - 1]
        self.my_set[self.my_arr[len(self.my_arr) - 1]] = idx
        self.my_arr.pop()

        self.my_set.pop(val)

        return True
        

    def getRandom(self) -> int:
        if len(self.my_set) == 0:
            return -1

        rand = random.randint(0, len(self.my_set) - 1)
        return self.my_arr[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()