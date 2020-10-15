class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = collections.defaultdict(int)
        for i in s:
            count_dict[i] += 1
        
        result = []
        for key, value in sorted(count_dict.items(), key = lambda item: item[1], reverse = True):
            result.extend([key] * value)
        
        return "".join(result)