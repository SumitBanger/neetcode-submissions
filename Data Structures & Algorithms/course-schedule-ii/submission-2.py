class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result, visited, completed = False, set(), []
        preReqMap = {i:[] for i in range(numCourses)}
        for [course, preq] in prerequisites:
            preReqMap[course].append(preq)

        def dfs(current):
            if current in visited: # We found a loop so return False
                return False

            if preReqMap[current] == []:
                if current not in completed:
                    completed.append(current)
                return True
            
            visited.add(current)
            for preq in preReqMap[current]:
                if not dfs(preq): return False
            preReqMap[current] = []
            completed.append(current)
            visited.remove(current)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []

        return completed     