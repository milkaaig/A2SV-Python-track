class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "". join(s.split())
        checker = []
        
        for i in s:
            if  i.isalnum():
                checker.append(i)
        
        l = 0
        r = len(checker) - 1
        
        while l <= r:
            if checker[l].lower() != checker[r].lower():
                return False
            l += 1
            r -= 1
            
        return True