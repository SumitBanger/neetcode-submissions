class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencyMap, time, taskQ = {}, 0, deque()
        for task in tasks:
            frequencyMap[task] = frequencyMap.get(task, 0) + 1
        
        taskCountList = [count for taskName, count in frequencyMap.items()]

        heapq.heapify_max(taskCountList)

        while len(taskCountList) > 0 or taskQ:
            if taskQ and time == taskQ[0][1]:
                poppedTask = taskQ.popleft()[0]
                heapq.heappush_max(taskCountList, poppedTask)

            if len(taskCountList) > 0:
                currentMaxTaskCount = heapq.heappop_max(taskCountList)
                currentMaxTaskCount -= 1
                if currentMaxTaskCount > 0:
                    taskQ.append([currentMaxTaskCount, time + n + 1])
            
            time += 1   

        return time



        

        