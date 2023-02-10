class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(height) - 1
        
        while l < r :
#             min because we are forming a container (to no create imbalance of rectangle)
            y = min(height[r] , height[l])
            x = r - l
            area =  x * y
            
            if area > maxarea:
                maxarea = area
            
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
                
        return maxarea
            
            