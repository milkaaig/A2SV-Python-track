class Solution:
    def __init__(self):
        self.output = []
        

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.length = len(s)
        path = []
        self.checker(s, path, 0)
        return self.output


        
    def checker(self, s, path, idx ):
        if len(path) == 4 and len('.'.join(path.copy())) == self.length + 3:          
            
            self.output.append('.'.join(path.copy()))
            
        if idx >= self.length:
            return
        
        for i  in range(idx, self.length):
            temp = s[idx : i + 1]
           
            if len(temp) > 1 and temp[0] == '0':
                continue
           
            if  int(temp) < 0 or int (temp) > 255 or len(temp) > 3 :
                continue
           

            
            path.append(temp)
            self.checker(s, path, i + 1)
            path.pop()