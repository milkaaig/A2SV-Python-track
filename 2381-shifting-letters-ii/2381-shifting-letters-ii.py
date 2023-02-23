class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * len(s)
        output = ''
       
        for a, b, k in shifts:
            if k == 0:
                k = -1
            arr[a] += k
            
            if b + 1 < n:
                arr[b + 1] -= k

        for i in range(1, n):
            arr[i] += arr[i - 1]
            
        for i in range(n):
            arr[i] %= 26
            
        for i  in range(n):
            j = ord(s[i]) + arr[i]
            
            if j > 122:
                j -= 26
            
            output += chr(j)
            
        return output