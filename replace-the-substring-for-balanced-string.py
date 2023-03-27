class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        bal = n // 4
        dic = Counter(s)
        record = {}
        count = 0

        for k, v in dic.items():
            if v > bal:
                record[k] = v - bal
                count += 1
        
        if count == 0:
            return 0

        minm = n
        left = 0
       
        window = defaultdict(int)
    
        for right in range( n):
            window[s[right]] += 1

            t = count
               
            for k, v in record.items():
                if record[k] <= window[k] :
                    t -= 1
            
            while left <= right and t == 0:
                minm = min(minm, (right - left) + 1)
                window[s[left]] -= 1
                
                if s[left] in record and window[s[left]] < record[s[left]]:
                    t += 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

        return minm