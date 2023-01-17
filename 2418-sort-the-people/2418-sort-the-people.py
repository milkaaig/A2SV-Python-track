class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # size = len(array)
        # for i in range(size):
        #     for j in range(i, size - 1):
        # if array[j] > array[j + 1]:
        # array[j], array[j + 1] = array[j + 1], array[j]
        size = len(names)
        
        for i in range(size-1):
            for j in range(size-1):
                
                if heights[j] < heights[j + 1] :
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j] , heights[j+1] = heights[j+1],heights[j]
            
        return names
    
    
        