class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = [[-h, k] for h, k in people]
        heapq.heapify(people)
        result = []
        while people:
            person = heapq.heappop(people)
            result = result[:person[1]] + [[-person[0], person[1]]] + result[person[1]:]
        return result