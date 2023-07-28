class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = defaultdict(list)

        for n in nums:
            if dic[n - 1]:
                # it is basically checking lenght of the subsequence before the current number and then adding that length to the current one removing the previous. it keeps the length of consecutive subsequences
                heappush(dic[n], heappop(dic[n - 1]) + 1)
                
            else:
                heappush(dic[n], 1)
        
        for lst in  dic.values():
            for i in lst:
                if i < 3:
                    return False
            
        return True