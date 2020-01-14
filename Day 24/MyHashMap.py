# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash_map = [[] for i in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        location = self.hash(key)
        if not self.hash_map[location]:
            self.hash_map[location].append([key, value])
        else:
            found = False
            for i in self.hash_map[location]:
                if key == i[0]:
                    found = True
                    i[1] = value
                    break
            if not found:
                self.hash_map[location].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        location = self.hash(key)
        if self.hash_map[location] == []:
            return -1
        for i in self.hash_map[location]:
            if key == i[0]:
                return i[1]
        return -1
    
    def hash(self, key):
        return key % self.size

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        location = self.hash(key)
        value = self.get(key)
        print(key, value, self.hash_map[location])
        if value != -1:
            self.hash_map[location].remove([key, value])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
