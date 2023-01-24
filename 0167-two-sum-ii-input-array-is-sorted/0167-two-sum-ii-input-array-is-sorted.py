class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ns = len(numbers)
        l = 0 
        r = ns-1
        
        while  r > l:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            elif sum == target:
                return [l +1 , r + 1]
               
                
        