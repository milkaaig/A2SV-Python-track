class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        size = len(skill)
        r = size -1
        l = 0
        output = 0
        skill.sort()
        checker = skill[0] + skill[-1]
        
        for i in range(size // 2):
            if skill[l] + skill[r] != checker:
                return -1
            output += (skill[l] * skill[r]) 
            l += 1
            r -= 1
            
        
        return output
            