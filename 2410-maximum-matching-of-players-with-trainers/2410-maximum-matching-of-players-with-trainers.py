class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        numt = len(trainers)
        nump = len(players)
        players.sort()
        trainers.sort()
        ppt = 0
        ptr = 0
        output = 0
        
        while  ptr < numt:
            if ppt == nump:
                break
                
            if players[ppt] <= trainers[ptr]:
                output += 1
                ptr += 1
                ppt += 1
            elif players[ppt] > trainers[ptr]:
                ptr += 1
        
        return output
        