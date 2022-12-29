class Solution:
    def freqAlphabets(self, s: str) -> str:
        alps = "abcdefghijklmnopqrstuvwxyz"
        ptr = 0
        lens = len(s)
        maps = ""
        ss = ""
        while ptr < lens:
           
            if ptr+2 < lens and s[ptr + 2] == '#':
                ss = ""
                ss += s[ptr]
                ss += s[ptr +1]
                sss = int(ss)
                maps += alps[sss-1]
                ptr += 3
            else:
                ss = int(s[ptr])
                maps += alps[ss-1]
                ptr += 1
        return maps
            