class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totPoints = len(points)
        adj_list = {i: [] for i in range(totPoints)}
        for src in range(totPoints):
            srcPoint = points[src]
            for dest in range(src + 1, totPoints):
                destPoint = points[dest]
                distance = abs(destPoint[0] - srcPoint[0]) + abs(destPoint[1] - srcPoint[1])
                adj_list[src].append((distance, dest))
                adj_list[dest].append((distance, src))
            
        cost, minHeap, visited = 0, [(0,0)], set()
        while minHeap:
            distance, src = heapq.heappop(minHeap)
            if src in visited:
                continue

            if src not in visited:
                visited.add(src)
                cost += distance

            if len(visited) == totPoints:
                return cost
            
            for neighborDist, neighbor in adj_list[src]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (neighborDist, neighbor))

        