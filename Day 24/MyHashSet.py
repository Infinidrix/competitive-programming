# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash_set = [[] for i in range(self.size)]
        
    def hash(self, key):
        return key % self.size
        
        
    def add(self, key: int) -> None:
        loc = self.hash(key)
        if self.hash_set[loc] == [] or key not in self.hash_set[loc]:
            self.hash_set[loc].append(key)
            
    def remove(self, key: int) -> None:
        loc = self.hash(key)
        if self.contains(key):
            self.hash_set[loc].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        loc = self.hash(key)
        if key in self.hash_set[loc]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
