
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda task : task[1] - task[0])
        used = all_energy = 0
        for index in range(len(tasks) - 1, -1, -1):
            task = tasks[index]
            spare = all_energy - used
            if task[1] > spare:
                all_energy += task[1] - spare
            used += task[0]
        return all_energy
