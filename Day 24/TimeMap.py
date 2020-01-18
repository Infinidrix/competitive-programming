# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_store = {}
        self.hash_store = {}

    def find_nearest_timestamp_old(self, key, timestamp):
        nearest = -1
        for i in range(len(self.key_store[key])):
            if self.key_store[key][i] > timestamp:
                break
            nearest = self.key_store[key][i]
        return nearest
    
    def find_nearest_timestamp(self, key, timestamp, start, end):
        search_list = self.key_store[key]
        while start < end:
            mid = start + (end - start) // 2
            if search_list[mid] == timestamp:
                return search_list[mid]
            elif search_list[mid] < timestamp:
                start = mid + 1
            else:
                end = mid - 1
        if start == 0 and search_list[0] > timestamp:
            return -1
        if search_list[end] <= timestamp:
            return search_list[end]
        return search_list[mid]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_store:
            self.key_store[key].append(timestamp)
        else:
            self.key_store[key] = [timestamp]
        self.hash_store[key+str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key_store:
            nearest_timestamp = self.find_nearest_timestamp(key, timestamp, 0, len(self.key_store[key]) - 1)
            if nearest_timestamp != -1:
                return self.hash_store[key+str(nearest_timestamp)]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
