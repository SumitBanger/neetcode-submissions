class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        temp_prices = prices.copy()

        for stop in range(k + 1):
            for src, dest, price in flights:
                if prices[src] == float("inf"): # Skip the unreacheable Nodes
                    continue
                
                temp_prices[dest] = min(temp_prices[dest], prices[src] + price)
            
            prices = temp_prices.copy()
        
        return -1 if prices[dst] == float("inf") else prices[dst]