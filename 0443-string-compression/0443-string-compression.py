class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        
        if len(chars) == 1:
            return 1
        
        ct = 0
        s = []
        l = chars[0]
        chars.append("-")
        
        for i in range(len(chars)):
            print(ct)
            if chars[i] == l:
                ct += 1
            else:
                l = chars[i] 
                
                if ct == 1:
                    s.append(chars[i - 1])
                else:
                    s.append(chars[i - 1])
                    cc = str(ct)
                    for i in range(len(cc)):
                        s.append(cc[i])

                ct = 1  
                
            
        # print(s)
        chars.clear()
        for i in s:
            chars.append(i)
        return len(chars)
                
            
        