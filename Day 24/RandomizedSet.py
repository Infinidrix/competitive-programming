import random

# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = set()
        self.all_store = []
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.store:
            self.store.add(val)
            self.all_store.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.store:
            self.store.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        while True:
            if len(self.all_store) == 1:
                chosen = 0
            else:
                chosen = random.randint(0, len(self.all_store) - 1)
            if self.all_store[chosen] in self.store:
                return self.all_store[chosen]
            self.all_store.pop(chosen)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
