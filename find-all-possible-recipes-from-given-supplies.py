class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for  i in range(n):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                incoming[recipes[i]] += 1
        
        que = deque()
        output = [] 
        que.extend(supplies)
        recipes = set(recipes)

        while que:
            ingred = que.pop()
            
            if ingred in recipes:
                output.append(ingred)

            for node in graph[ingred]:
                incoming[node] -= 1
                
                if incoming[node] == 0:
                    que.append(node)
        
        return output