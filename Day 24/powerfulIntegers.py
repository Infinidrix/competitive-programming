# https://leetcode.com/problems/powerful-integers/

class Solution:
    def find_multiples(self, x, bounds):
        x_multiples = [1]
        last_x = 0
        new_x = x
        while last_x != new_x and new_x <= bounds:
            x_multiples.append(new_x)
            last_x = new_x
            new_x *= x
        return x_multiples
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_multiples = self.find_multiples(x, bound)
        y_multiples = self.find_multiples(y, bound)
        result = set()
        for i in range(len(y_multiples)):
            broken = False
            for j in range(len(x_multiples)):
                if x_multiples[j] + y_multiples[i] <= bound:
                    result.add(x_multiples[j] + y_multiples[i])
                elif j == 0:
                    broken = True
                    break
                else:
                    break
            if broken:
                break
        return list(result)
