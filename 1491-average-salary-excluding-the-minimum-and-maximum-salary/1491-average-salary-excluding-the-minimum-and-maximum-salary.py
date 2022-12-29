class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        del salary[0]
        del salary[-1]
        emp = len(salary)
        Avgsal = 0
        for empsal in range(emp):
            Avgsal += salary[empsal]
        Avgsal /= emp
        return Avgsal