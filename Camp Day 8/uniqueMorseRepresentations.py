# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        translation = [".-","-...","-.-.", "-..",".","..-.","--.","....","..",".---", "-.-",".-..","--","-.","---", ".--.","--.-",".-.","...","-","..-", "...-",".--","-..-","-.--","--.."]
        
        unique = set()
        count = 0
        translated = []
        for i in words:
            new_morse = []
            for j in i:
                new_morse.append(translation[ord(j) - ord("a")])
            translated.append("".join(new_morse))
        for i in translated:
            if i not in unique:
                count += 1
                unique.add(i)
        return count
