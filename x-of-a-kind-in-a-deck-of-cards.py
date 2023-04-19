import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deckdic = defaultdict(int)
        dec = set()
        length = len(deck)

        if length == 1:
            return False

        for i in deck:
            deckdic[i] += 1
            dec.add(i)
        x = []
        
        for key, val in deckdic.items():
            x.append(val)

        gcd = math.gcd(*x)

        
        return gcd > 1