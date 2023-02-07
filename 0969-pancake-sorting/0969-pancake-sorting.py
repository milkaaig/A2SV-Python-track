class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        l = 0
        r = len(arr) 
        
        while r > 0 and sorted(arr) != arr:
            # the location of the biggest number and add 1 cz it is zero indexed
            k = arr.index(r) + 1
            z = arr[l : k]   
            # reverse that section
            z.reverse()
            output.append(k)
            # append  the reversed section to the array and check if it is sorted
            arr[ l : k] = z
            
            if sorted(arr) == arr:
                break
                
            rev = arr[l : r]
            rev.reverse()
            arr[l : r] = rev
            output.append(r)
            r -= 1
            
                
        return output
           
                