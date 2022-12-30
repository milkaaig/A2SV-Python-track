class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrl = len(arr)
        for i in range(arrl):
            for j in range(arrl):
                print(arr[i],2 *arr[j])
                if i == j:
                    continue
                if arr[i] == 2 * arr[j]:  
                    return True
                    
        return False
                     