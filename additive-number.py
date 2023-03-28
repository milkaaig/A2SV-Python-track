class Solution:
    
        
    def isAdditiveNumber(self, num: str) -> bool:
        self.length = len(num)
        path = []
        return self.checker(0, path, num)


    def checker(self,idx,path, nums ):
        if len(path) >= 3 and idx >= self.length:
            return True
        
        for i in range(idx , self.length):
            temp = nums[idx : i + 1]

            if len(temp) > 1 and temp[0] == '0':
                continue
            
            if len(path) >= 2:
                
                if path[-1] + path[-2] == int(temp):
                    path.append(int(temp)) 
                    if self.checker(i + 1,path, nums):
                        return True
                    path.pop()
                
            else:
                path.append(int(temp))
                if self.checker(i + 1,path, nums):
                        return True
                path.pop()
        
        return False