class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result, visited = False, set()
        preReqMap = {i:[] for i in range(numCourses)}
        for [a, b] in prerequisites:
            preReqMap[a].append(b)

        def dfs(current):
            if current in visited:
                return False

            if preReqMap[current] == []:
                return True
            
            visited.add(current)
            for preq in preReqMap[current]:
                if not dfs(preq): return False
            preReqMap[current] = []
            visited.remove(current)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False

        #print(preReqMap)
        return True
        