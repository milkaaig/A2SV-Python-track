class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26)]
        self. isEOW = False

    
class Solution:
    


    def __init__(self):
        self.root = TrieNode()
    
    def insertFirst(self, word: str) -> None:
        node = self.root

        for char in word:
            i = ord(char) - ord('a')

            if not  node.children[i]:
                node.children[i] = TrieNode()

            node = node.children[i]

        node.isEOW = True


    def insert(self, word: str):
        node = self.root
        count = ''
        for char in word:
            i = ord(char) - ord('a')

            if not  node.children[i] or node.isEOW:
                break
            else:
                count += char

            node = node.children[i]

        node.isEOW = True

        return count
        

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            i =  ord(char) - ord('a')

            if not node.children[i]:
                return False
            
            node = node.children[i]
        return node.isEOW
        

    def startsWith(self, prefix: str) -> bool:
        node = self. root

        for char in prefix:
            i = ord(char) - ord('a')

            if not node.children[i]:
                return False
                
            node = node.children[i]

        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:

        output = ''
        length = len(strs)

        if length == 1:
            return strs[0]
            
        self.insertFirst(strs[0])

        for word in strs[1:]:
            output = self.insert(word)
            


        return output

        
        