class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        size = len(people)
        l = 0
        r = size - 1 
        output = 0
        
        while l <= r:
            if people[l] + people[r] <= limit:

                    l += 1
                    r -= 1

            else:
                    r -= 1
                    
            output += 1   
                
        
        return output
        
        
            
        