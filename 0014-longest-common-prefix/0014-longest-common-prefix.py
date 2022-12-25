class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        checker = min(strs)  
        for strings in strs:
            while len(strings):
                if strings.startswith(checker):
                    break
                else:
                    checker=checker[:-1]
        return checker
        