class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        size = len(tokens)
        stack = []
        symbols = ["+", "-", "*", "/"]

        def calculate(b: int, a: int, c: str) -> int:
            if c == '+':
                return b + a
            elif c == '-':
                return b - a
            elif c == '*':
                return b * a
            elif c == '/':
                return trunc(b / a)

            return -1
    
        
        for token in tokens:

            if token in symbols:
                a = int(stack.pop())
                b = int(stack.pop())
                output = calculate(b, a, token)
                stack.append(output)
            else:
                stack.append(int(token))

        return stack[-1]