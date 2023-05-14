class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        output = []
        isReachable = defaultdict(bool)

        for pre, course in prerequisites:
            graph[pre].append(course)
        
        def checker(pre, course):
            if pre == course:
                return True

            if (pre, course) in isReachable:
                return isReachable[(pre, course)]
            
           
            for courses in graph[pre]:
                if checker(courses, course):
                    isReachable[(courses, course)] = True
                    return True
            
            isReachable[(pre, course)] = False
            
            return False

       
        for pre, course  in queries:
            if checker(pre, course):
                output.append(True)
            else:
                output.append(False)
            
        
        return output