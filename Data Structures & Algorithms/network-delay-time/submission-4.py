class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list, visited = {i: [] for i in range(n + 1)}, set()
        for src, dest, time in times:
            adj_list[src].append((dest, time))

        minHeap, totalTime = [(0, k)], 0
        while minHeap:
            nodeTime, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            totalTime = max(totalTime, nodeTime)

            # if len(visited) == n:
            #     return totalTime

            for neighbor, neighborTime in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (nodeTime + neighborTime, neighbor))
        
        return totalTime if len(visited) == n else -1
