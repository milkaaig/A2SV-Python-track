class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)
        mount = 0
        
        if size < 3:
            return False
        inc = 0
        while inc < size-1:
            if arr[inc] > arr[inc + 1]:
                mount = inc
                break
            elif arr[inc] == arr[inc + 1]:
                return False
            inc += 1
        if mount != 0:
            dec = mount
            while dec < size -1:
                if arr[dec] < arr[dec+1]:
                    return False
                elif arr[dec] == arr[dec + 1]:
                     return False
                dec += 1
            return True
        else: 
            return False
            
            
        
            