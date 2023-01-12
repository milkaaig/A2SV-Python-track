from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        firstword =set(words[0])
        thelist = []
        output = []
        for char in firstword:
            miny = min([word.count(char) for word in words])
            if miny > 0:
                output += [char]*miny
       
        return output