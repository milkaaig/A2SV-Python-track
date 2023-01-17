class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        for i in range(size):
            maxm = i
            for j in range(i+1, size):
                if heights[j] > heights[maxm]:
                    maxm = j
            heights[i], heights[maxm] = heights[maxm], heights[i]
            names[i], names[maxm] = names[maxm], names[i]
            
        return names
    
    
        