class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceToPointTuples = []
        result = []
        for point in points:
            [x, y] = point
            distance = math.sqrt(x*x + y*y)
            distanceToPointTuples.append((distance, point))
        
        heapq.heapify_max(distanceToPointTuples)
        while len(distanceToPointTuples) > k:
            heapq.heappop_max(distanceToPointTuples)

        result1 = [distanceToPointTuple[1] for distanceToPointTuple in distanceToPointTuples]

        for distanceToPointTuple in distanceToPointTuples:
            result.append(distanceToPointTuple[1])
        
        return result1