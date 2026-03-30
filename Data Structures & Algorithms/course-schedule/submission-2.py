class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            preMap[course].append(preReq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True

            visiting.add(course)

            for preReq in preMap[course]:
                if not dfs(preReq):
                    return False
            
            visiting.remove(course)
            preMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True