class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result, visited, completed, completed_set = False, set(), [], set()
        preReqMap = {i:[] for i in range(numCourses)}
        for [course, preq] in prerequisites:
            preReqMap[course].append(preq)

        def dfs(current):
            if current in visited: # We found a loop so return False
                return False

            if current in completed_set:
                return True
            if preReqMap[current] == []:
                completed.append(current)
                completed_set.add(current)
                return True
            
            visited.add(current)
            for preq in preReqMap[current]:
                if not dfs(preq): return False
            preReqMap[current] = []
            completed.append(current)
            completed_set.add(current)
            visited.remove(current)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []

        return completed   