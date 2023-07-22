from collections import defaultdict
from typing import List

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = defaultdict(int)
        self.graph = defaultdict(list)

        for i in range(1, len(self.parent)):
            self.graph[self.parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False

        self.locked[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # Check ancestors
        def ancestors(node):
            if self.locked[node]:
                return False

            if node == -1:
                return True

            return ancestors(self.parent[node])  

        if not ancestors(num):
            return False

        # Check children
        def children(node):
            for child in self.graph[node]:
                if self.locked[child] or children(child):  
                    return True

            return False

        if not children(num):
            return False

        # Unlocking
        def unlocking(node):
            for child in self.graph[node]:
                if self.locked[child]:
                    self.locked[child] = 0  
                unlocking(child)

            return True  

        unlocking(num)
        self.locked[num] = user

        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)