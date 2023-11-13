class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        alive = [0] * 101
        
        for log in logs:
            birth = log[0] - 1950
            death = log[1] - 1950
            
            for i in range(birth, death):
                alive[i] += 1
        
        maxpop = 0
        earliest = 0
        
        for year in range(101):
            # print(year)
            if alive[year] > maxpop:
                maxpop = alive[year]
                earliest = year
        
        return earliest + 1950
            
        