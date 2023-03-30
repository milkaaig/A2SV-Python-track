class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        output = set()
        length = len(s)

       
        checker = set()
        left = 0
        right = 10

        while right <= length:
            print(2)
            window = s[left : right]
            if window in checker :
                output.add(window)
            else:
                checker.add(window)

            right += 1
            left  += 1
        
        return list(output)