class Solution:         
    def countMaxOrSubsets(self, nums):
        n = len(nums)
        dic = defaultdict(int)

        def checker(index, maxm):
            #keep track of all the bitwise or you get 
            dic[maxm] += 1

            for i in range(index,n):
                #every possible bitwise OR subset you get
                checker(i+1, maxm|nums[i])

        checker(0,0)
        #how many times did the maximum bitwise or appear 
        return dic[max(dic.keys())]