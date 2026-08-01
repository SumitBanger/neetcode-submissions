class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, visited = len(grid), set()
        minHeap = [(grid[0][0], 0, 0)] # Stores time/max-height & x, y coordinates of block
        visited.add((0,0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return time
            
            for dr, dc in directions:
                row, col = r + dr, c + dc

                if (row in range(N)) and (col in range(N)) and ((row, col) not in visited):
                    heapq.heappush(minHeap, (max(time, grid[row][col]), row, col))
                    visited.add((row, col))
        return -1