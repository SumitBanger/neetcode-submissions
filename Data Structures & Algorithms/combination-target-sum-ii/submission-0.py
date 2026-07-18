class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)

        result, combination = [], []

        def dfs(index, currentSum):
            if currentSum == target:
                result.append(combination.copy())
                return
            if currentSum > target or index >= len(nums):
                return

            combination.append(nums[index]) # Take element at index position
            # while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            #     index += 1
            dfs(index + 1, currentSum + nums[index]) # Do DFS including current element
            
            combination.pop() # backtrack - Pop the above added element
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, currentSum) # Do DFS excluding current element
        
        dfs(0, 0)
        return result

        