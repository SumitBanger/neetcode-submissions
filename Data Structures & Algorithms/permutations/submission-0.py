class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, combination = [], []
        numbers = set(nums)
        def dfs(numbers):
            if len(numbers) == 0:
                result.append(combination.copy())
                return

            for num in list(numbers):
                combination.append(num) # select num
                numbers.remove(num)
                dfs(numbers)

                combination.pop() # backtrack
                numbers.add(num)
        
        dfs(numbers)
        return result


        