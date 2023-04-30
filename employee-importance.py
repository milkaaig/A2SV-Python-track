"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # create a dictionary to store employee objects by id
        empd = defaultdict(int)

        for emp in employees:
            empd[emp.id] = emp
        
      
        def calculate(eid):
            emp = empd[eid]
            subimp = 0
            for sub in emp.subordinates:
                subimp += calculate(sub)
                
            return emp.importance + subimp
        
        return calculate(id)