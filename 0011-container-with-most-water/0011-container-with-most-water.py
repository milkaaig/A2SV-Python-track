class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        r = 0
        l = len(height) - 1
        
        while r < l :
#             min because we are forming a container (to no create imbalance of rectangle)
            y = min(height[r] , height[l])
            x = l - r
            area =  x * y
            
            if area > maxarea:
                maxarea = area
            
            if height[r] < height[l]:
                r += 1
            else:
                l -= 1
                
        return maxarea
            
            