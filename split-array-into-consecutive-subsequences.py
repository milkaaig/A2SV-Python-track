class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = defaultdict(list)

        for n in nums:
            if dic[n - 1]:
                heappush(dic[n], heappop(dic[n - 1]) + 1)
            else:
                heappush(dic[n], 1)

        for lst in  dic.values():
            for i in lst:
                if i < 3:
                    return False
            # if sum(lst) < len(lst) * 3 :
            #     return False
        return True