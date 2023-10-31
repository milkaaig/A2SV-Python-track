class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        length = len(pref)
        output = [pref[0]]
        
        for i in range(1, length):
            original = pref[i] ^ pref[i - 1]
            output.append(original)
        
        return output