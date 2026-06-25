class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            heavier = heapq.heappop_max(stones)

            if heaviest > heavier:
                heapq.heappush_max(stones, heaviest - heavier)
            
        return stones[0] if stones else 0
        