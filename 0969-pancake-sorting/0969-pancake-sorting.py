class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []

        l = 0
        r = len(arr) 
        
        while r > 0 and sorted(arr) != arr:
            k = arr.index(r) + 1
            z = arr[l : k]        
            z.reverse()
            output.append(k)
            arr[ l : k] = z
            
            if sorted(arr) == arr:
                break
                
            z = arr[l : r]
            z.reverse()
            arr[l : r] = z
            output.append(r)
            r -= 1
            
                
        return output
           
                