class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        count_temp = [[] for i in range(71)]
        for i in range(len(T)):
            count_temp[T[i]-30].append(i)
        result = []
        for i in range(len(T)):
            mini = 30001
            for j in range(T[i]-29, 71):
                while count_temp[j] != [] and count_temp[j][0] < i:
                    count_temp[j].pop(0)
                if count_temp[j] != [] and 0 < count_temp[j][0] - i < mini:
                    mini = count_temp[j][0] - i
            result.append(mini%30001)
        return result
            