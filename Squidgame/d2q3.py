class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            if log[-1].islower():
                letter.append(list(reversed(log.split(" ", 1))))
            else:
                digit.append(log)

        return list(map(lambda x: " ".join(reversed(x)), sorted(letter))) + digit