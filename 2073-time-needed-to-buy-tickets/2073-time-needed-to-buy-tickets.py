class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        output = 0
        size = len(tickets)
        
        for i in range(size):
            if i == k:
                index = i
                break
                
        i = 0
        
        while tickets[index] > 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                output += 1 

            i += 1
            
            if i == size:
                i = 0
            
        return output
            
           
        