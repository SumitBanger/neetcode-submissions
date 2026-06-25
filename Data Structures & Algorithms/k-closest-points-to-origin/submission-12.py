import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This is optimal O(n) Solution using quick select algo
        return self.quickSelectSolution(points, k)

        # Below is sub-optimal O(klogn) solution
        result = []
        distanceToPoints = [(x*x + y*y, [x, y]) for x, y in points]
        
        heapq.heapify(distanceToPoints)
        for _ in range(k):
            result.append(heapq.heappop(distanceToPoints)[1])
        return result
        
    def quickSelectSolution(self, points, k):
        self.selection(0, len(points) - 1, points, k)
        return points[:k]

    def selection(self, left, right, points, k):
        if left >= right: return
        pivot_idx = self.partition(left, right, points)

        if pivot_idx == k:
            return
        elif pivot_idx > k:
            self.selection(left, pivot_idx - 1, points, k)
        else:
            self.selection(pivot_idx + 1, right, points, k)
    
    def partition(self, left, right, points):
        # 0. Select Random Pivot point & Calc its Distance
        pivot_idx = random.randint(left, right)
        pivot_dist = self.getDist(points[pivot_idx])
        # 1. Move pivot out of the way to the right end
        points[pivot_idx], points[right] = points[right], points[pivot_idx]  
        # 2. Move all points closer than the pivot to the left
        store_idx = left
        for index in range(left, right):
            if self.getDist(points[index]) < pivot_dist:
                points[index], points[store_idx] = points[store_idx], points[index]
                store_idx += 1
        # 3. Swap rightmost point (Pivot) to the actual index for pivot - i.e Current Store Idx
        points[right], points[store_idx] = points[store_idx], points[right]
        return store_idx 

    def getDist(self, point):
        x, y = point
        return ((x*x) + (y*y))
    



