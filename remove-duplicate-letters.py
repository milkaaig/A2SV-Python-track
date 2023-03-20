class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        ss = len(s)
        dic = {}
        onepiece = set()

        for i in range(ss):
            dic[s[i]] = i
        
        for n, char in enumerate(s):

            if char not in onepiece:

                while stack and stack[-1] > char and dic[stack[-1]] > n:
                    onepiece.remove(stack[-1])
                    stack.pop()
                
                stack.append(char)
                onepiece.add(char)
        
        return "".join(stack)