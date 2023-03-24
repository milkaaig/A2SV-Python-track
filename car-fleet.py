class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        length = len(position)
        match = []

        for i in range(length):
            match.append([position[i], speed[i]])
        
        match.sort(reverse = True)

        for p, s  in match:
            t = (target - p) / s

            if stack == [] or stack[-1] < t:
                stack.append(t)
            

        return len(stack)