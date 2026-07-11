class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subsets = [], []

        def dfs(index):
            if index >= len(nums):
                result.append(subsets.copy())
                return
            dfs(index + 1) # skip
            subsets.append(nums[index])
            dfs(index + 1) # take
            subsets.pop() # Pop to leave subsets state same as it was at the start of call
            #dfs(index + 1)
    
        dfs(0)
        return result



        