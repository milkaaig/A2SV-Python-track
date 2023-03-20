class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(left, right, turn):
            if left == right:
                if turn:
                    return [nums[left], 0]

                return [0, nums[right]]
            
            if turn:
                out1 = winner(left + 1, right, not turn)
                out1[0] += nums[left]
                out2 = winner(left, right -1, not turn)
                out2[0] += nums[right]

                if out1[0] >= out2[0]:
                    return out1

                return out2
            else:
                out1 = winner(left + 1, right, not turn)
                out1[1] += nums[left]
                out2 = winner(left, right -1, not turn)
                out2[1] += nums[right]

                if out1[1] >= out2[1]:
                    return out1
                    
                return out2

        output = winner(0, len(nums) - 1, True)

        if output[0] >= output[1]:
            return True
            
        return False