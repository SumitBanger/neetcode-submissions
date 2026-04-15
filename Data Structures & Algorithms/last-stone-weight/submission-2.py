class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            nextHeaviest = heapq.heappop_max(stones)

            if heaviest > nextHeaviest:
                heapq.heappush_max(stones, heaviest - nextHeaviest)

            
        return stones[0] if len(stones) == 1 else 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        heapq.heapify_max(stones)
        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            secondLargest = heapq.heappop_max(stones)
            if largest > secondLargest:
                heapq.heappush_max(stones, largest - secondLargest)
        
        return stones[0] if len(stones) == 1 else 0