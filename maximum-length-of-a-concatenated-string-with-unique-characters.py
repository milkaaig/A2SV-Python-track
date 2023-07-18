class Solution:
    def maxLength(self, arr: List[str]) -> int:
        check = ['']
        output = 0
        
        for i in range (len(arr)):
            for j in range(len(check)):
                conct = arr[i] + check[j]
                
                # to make sure there are no repeated characters in every combo
                if len(conct) == len(set(conct)):
                    check.append(conct)
                    output = max(len(conct), output)
                
        return output