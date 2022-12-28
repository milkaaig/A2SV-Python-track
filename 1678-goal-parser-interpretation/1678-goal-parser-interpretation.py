class Solution:
    def interpret(self, command: str) -> str:
        length = len (command)
        intpcmd = ''
        for i in range(length):
            if command[i]== '(' and command[i+1] == ')':
                intpcmd += 'o'
            elif command[i]== 'G' :
                intpcmd += 'G'
            elif command[i] == '(' and command[i + 1] == 'a':
                intpcmd += 'al'
            else:
                 continue
        return intpcmd

            
  