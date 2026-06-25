class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceToPoints, result = [], []
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            distanceToPoints.append((self.findDistance(x1, y1), points[i]))
        
        heapq.heapify(distanceToPoints)
        print(f"distanceToPoints: {distanceToPoints}")
        for _ in range(k):
            result.append(heapq.heappop(distanceToPoints)[1])
        return result

    def findDistance(self, x1, y1):
        distance = math.sqrt((x1*x1) + (y1*y1))
        print(f"points x1: {x1}, y1: {y1}, distance: {distance}")
        return distance
        