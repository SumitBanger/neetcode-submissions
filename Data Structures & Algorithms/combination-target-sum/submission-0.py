class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, combination = [], []

        def dfs(index, currentSum):
            if currentSum == target:
                result.append(combination.copy())
                return
            
            if currentSum > target or index >= len(nums):
                return

            combination.append(nums[index]) # Take element at index position
            dfs(index, currentSum + nums[index]) # Do DFS including current element
            
            combination.pop() # backtrack - Pop the above added element
            dfs(index + 1, currentSum) # Do DFS excluding current element
        
        dfs(0, 0)
        return result