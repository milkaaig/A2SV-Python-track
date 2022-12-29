class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lngarr = len(arr)
        ptr = 0
        while ptr < lngarr:
            if arr[ptr] == 0:
                arr[ptr + 1:ptr +2 ]=[0,arr[ptr +1]]
                ptr += 2
            else:
                ptr += 1
        arr2 = arr[:lngarr]
        arr[:] = arr2[:]
            
        
        