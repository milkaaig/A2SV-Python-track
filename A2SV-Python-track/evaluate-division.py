class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(dict)
        length = len(equations)

        for i in range(length):
            div, den = equations[i]

            dic[div][den] = values[i]
            dic[den][div] = 1 / values[i]
        


        def dfs(div, den,seen):
            if div in seen or div not in dic:
                return -1.0
            
            if div == den:
                return 1.0
            
            seen.add(div)

            for divisor, val in dic[div].items():
                res  = dfs(divisor, den, seen)

                if res != -1.0:
                    return val * res
            
            return -1.0
        output = []

        for div, den in queries:
            output.append(dfs(div, den, set()))

        return output
