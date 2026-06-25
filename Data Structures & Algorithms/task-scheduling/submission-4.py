class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskToCountMap, totalTime = {}, 0
        for task in tasks:
            taskToCountMap[task] = taskToCountMap.get(task, 0) + 1

        maxHeap, queue = [], deque()
        for task, count in taskToCountMap.items():
            maxHeap.append((count, task))
        heapq.heapify_max(maxHeap)
        while True:
            if len(maxHeap) == 0 and len(queue) == 0:
                break
            totalTime += 1
            if maxHeap:
                count, task = heapq.heappop_max(maxHeap)
                if count > 1:
                    nextEntryForTask = totalTime + n
                    queue.append((nextEntryForTask, (count - 1, task)))
            if queue and totalTime == queue[0][0]:
                heapq.heappush_max(maxHeap, queue.popleft()[1])

        return totalTime

        