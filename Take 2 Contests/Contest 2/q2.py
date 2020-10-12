class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text_length = sorted([(len(i), i) for i in text.split(" ")], key=lambda item: item[0])
        new_text = " ".join([i[1] for i in text_length])
        
        return new_text.capitalize()