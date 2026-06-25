class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskToCountMap, totalTime = {}, 0
        for task in tasks:
            taskToCountMap[task] = taskToCountMap.get(task, 0) + 1

        maxHeap, queue = [], deque()
        for task, count in taskToCountMap.items():
            maxHeap.append((count, task))
        heapq.heapify_max(maxHeap)
        while maxHeap or queue:
            totalTime += 1
            count, task = heapq.heappop_max(maxHeap) if maxHeap else (1, "IDLE")
            if count > 1:
                nextEntryForTask = totalTime + n
                queue.append((nextEntryForTask, (count - 1, task)))
            if queue and totalTime == queue[0][0]:
                heapq.heappush_max(maxHeap, queue.popleft()[1])

        return totalTime

        