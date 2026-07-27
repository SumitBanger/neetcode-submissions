class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result, visited, completed = False, set(), set()
        preReqMap = {i:[] for i in range(numCourses)}
        for [a, b] in prerequisites:
            preReqMap[a].append(b)

        def dfs(current):
            if current in visited: # We found a loop so return False
                return False

            if current in completed:
                return True
            
            visited.add(current)
            preReq = preReqMap[current]
            while preReq:
                if not dfs(preReq[-1]): return False
                preReq.pop()
            completed.add(current)
            visited.remove(current)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False

        return True
        