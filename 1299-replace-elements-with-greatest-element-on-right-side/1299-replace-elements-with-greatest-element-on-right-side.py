class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        big= 0
        end = size - 1
        output = [0]*size
        for i in range(end, -1, -1):
            if i + 1 < size:
                if arr[i+1] > big:
                    big = arr[i + 1]
                    output[i] = big
                else: 
                    output[i] = big
            else:
                big = arr[i]
                output[i] = big
        output[-1] = -1
        return output