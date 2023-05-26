class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = defaultdict(int)
        for i in bills:
            print(wallet)
            print(i)
            
            if i == 10:
                if wallet[5] >= 1 :
                    wallet[5] -= 1
                    wallet[10] += 1
                else:
                    return False
                
            elif i == 20:
                if wallet[10] and wallet[5]:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                    
                else:
                    return False
    
            else:
                wallet[5] += 1
        return True