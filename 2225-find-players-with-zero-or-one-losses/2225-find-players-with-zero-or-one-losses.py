class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        length = len(matches)
        loserdic = {}
        winner = set()
        loser = []
        
        for i in range(length):
            if matches[i][1] in loserdic:
                loserdic[matches[i][1]] += 1
            else:
                loserdic[matches[i][1]] = 1
        for i in range(length):
            if matches[i][0] not in loserdic:
                winner.add(matches[i][0])
        for key,val in loserdic.items():
            if val  == 1:
                loser.append(key)
        winner = list(winner)
        loser.sort()
        winner.sort()
        answer =[winner,loser]
                
        
        return answer