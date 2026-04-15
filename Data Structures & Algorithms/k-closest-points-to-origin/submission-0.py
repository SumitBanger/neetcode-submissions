class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        result = []
        for point in points:
            [x, y] = point
            distance = math.sqrt(x*x + y*y)
            distances.append((distance, point))
        
        heapq.heapify_max(distances)
        while len(distances) > k:
            heapq.heappop_max(distances)

        for distance in distances:
            result.append(distance[1])

        
        return result