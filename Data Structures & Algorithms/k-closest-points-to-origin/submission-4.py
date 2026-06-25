class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceToPoints, result = [], []
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            distanceToPoints.append((self.findDistance(x1, y1), points[i]))
        
        heapq.heapify(distanceToPoints)
        for _ in range(k):
            result.append(heapq.heappop(distanceToPoints)[1])
        return result

    def findDistance(self, x1, y1):
        return math.sqrt((x1*x1) + (y1*y1))
        