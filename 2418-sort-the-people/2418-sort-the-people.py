class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        for i in range(size):
            while i > 0 and heights[i-1] < heights[i]:
                heights[i],heights[i-1] = heights[i-1],heights[i]
                names[i],names[i-1] = names[i-1],names[i]
                i -= 1
        return names
    
    
        