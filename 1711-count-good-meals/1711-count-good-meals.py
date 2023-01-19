class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        power = [0] *22
        powl = len(power)
        for i in range(powl):
            power[i] = math.pow(2,i)
       
        length = len(deliciousness)
        count = 0
        seen = {}
        
        for i in range(length):
            for j in range(powl):
                if power[j] - deliciousness[i] in seen:
                    count +=  seen[power[j] -  deliciousness[i]]
            if deliciousness[i] in seen:
                seen[deliciousness[i]] += 1
            else:
                seen[deliciousness[i]] = 1
     
        return count % (10**9 + 7)