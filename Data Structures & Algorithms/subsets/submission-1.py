class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subsets = [], []

        def DFS(index):
            if index >= len(nums):
                result.append(subsets.copy())
                return
            
            subsets.append(nums[index]) # Take the element at index position
            DFS(index + 1) 

            subsets.pop()         # Backtrack - Remove the just added element
            DFS(index + 1)

        DFS(0)
        return result;


        