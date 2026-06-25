class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceToPoints, result = [], []
        for x, y in points:
            dist = (x*x) + (y*y)
            distanceToPoints.append((dist, [x, y]))
        
        heapq.heapify(distanceToPoints)
        for _ in range(k):
            result.append(heapq.heappop(distanceToPoints)[1])
        return result
        