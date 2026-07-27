class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, completed_set, completed = set(), set(), []
        adj_list = {i:[] for i in range(numCourses)}
        preReqCount = [0] * numCourses
        for [course, preq] in prerequisites:
            adj_list[preq].append(course)
            preReqCount[course] += 1
        
        # 2. Queue all courses that have 0 prerequisites to start with
        queue = deque([course for course in range(numCourses) if preReqCount[course] == 0])
        while queue:
            course = queue.popleft()
            completed.append(course) # Mark course complete as we add only completed course in Q
            for dependent in adj_list[course]:
                preReqCount[dependent] -= 1
                if preReqCount[dependent] == 0: # If all the preq courses are complete i.e preReqCount is 0 it can be completed
                    queue.append(dependent)

        if len(completed) == numCourses:
            return completed
        return []

        # preReqMap = {i:[] for i in range(numCourses)}
        # for [course, preq] in prerequisites:
        #     preReqMap[course].append(preq)

        # def dfs(current):
        #     if current in visited: # We found a loop so return False
        #         return False

        #     if current in completed_set: # This course is already completed so return True
        #         return True

        #     if preReqMap[current] == []: # If this is a newly completed course then mark it so
        #         completed.append(current)
        #         completed_set.add(current)
        #         return True
            
        #     visited.add(current)
        #     for preq in preReqMap[current]:
        #         if not dfs(preq): return False
        #     preReqMap[current] = []
        #     completed.append(current)
        #     completed_set.add(current)
        #     visited.remove(current)
        #     return True
        
        # for i in range(numCourses):
        #     if not dfs(i): return []

        # return completed 