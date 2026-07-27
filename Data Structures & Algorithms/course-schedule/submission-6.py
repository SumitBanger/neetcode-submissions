class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result, visited, completed = False, set(), set()
        preReqMap = {i:[] for i in range(numCourses)}
        for [course, preq] in prerequisites:
            preReqMap[course].append(preq)

        def dfs(current):
            if current in visited: # We found a loop so return False
                return False

            if current in completed:
                return True
            
            visited.add(current)
            for preq in preReqMap[current]:
                if not dfs(preq): return False
            preReqMap[current] = []
            completed.add(current)
            visited.remove(current)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False

        return True
        