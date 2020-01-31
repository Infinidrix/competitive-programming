class Solution:
    
    def compute_value(self, domino):
        return domino[0] * 10 + domino[1]
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes.append([100, 100])
        matching_pairs = 0
        found_indexs = set()
        forward = sorted(dominoes, key = lambda domino: domino[0] * 10 + domino[1])
        reverse = [[forward[i][1], forward[i][0]] for i in range(len(forward)) if forward[i][0] != forward[i][1]]
        reverse = sorted(reverse, key = lambda domino: domino[0] * 10 + domino[1])
        reverse_i= 0
        #print(forward, reverse, sep='\n')
        i = 0
        while i < len(forward):
            j = 1
            while i+j < len(forward) - 1 and forward[i] == forward[i+j]:
                j+= 1
            if j != 1:
                matching_pairs += (j*(j-1))//2
            i += j
        #if forward[-1] == forward[-2]: matching_pairs += 1
        print("matching", matching_pairs)
        start = 0
        finish = 0
        for i in forward:
            if start >= len(reverse): break
            if str(i[0]) + str(i[1]) not in found_indexs:
                end = 0
                while start + end < len(reverse):
                    if self.compute_value(reverse[start+end]) < self.compute_value(i):
                        if finish <= start:
                            start += 1
                        else:
                            start = finish
                    elif self.compute_value(reverse[start+end]) == self.compute_value(i):
                        if finish <= start:
                            found_indexs.add(str(reverse[start+end][1])+str(reverse[start+end][0]))
                            end += 1
                            matching_pairs += 1
                        else:
                            end += finish - start
                            matching_pairs += finish - start
                    else:
                        finish = start + end
                        break
                
            
            
        #print(found_indexs)
        return matching_pairs
