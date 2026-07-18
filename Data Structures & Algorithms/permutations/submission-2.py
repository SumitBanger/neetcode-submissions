class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, combination = [], []
        used = [ False ] * len(nums)

        def dfs():
            if(len(combination) == len(nums)):
                result.append(combination.copy())
            for i in range(len(nums)):
                if used[i]: continue # We can't use already used elements
                
                combination.append(nums[i]) # Pick the current element and mark as used
                used[i] = True

                dfs()

                combination.pop() # backtrack - remove current element and unmark used
                used[i] = False

        dfs()
        return result


        # numbers = set(nums)
        # def dfs(numbers):
        #     if len(numbers) == 0:
        #         result.append(combination.copy())
        #         return

        #     for num in list(numbers):
        #         combination.append(num) # select num
        #         numbers.remove(num)
        #         dfs(numbers)

        #         combination.pop() # backtrack
        #         numbers.add(num)
        
        # dfs(numbers)
        # return result


        