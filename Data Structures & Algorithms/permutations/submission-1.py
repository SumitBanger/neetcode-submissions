class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, combination = [], []
        used = [ False ] * len(nums)

        def dfs():
            for i in range(len(nums)):
                if used[i]: continue
                combination.append(nums[i])
                used[i] = True

                dfs()

                if(len(combination) == len(nums)):
                    result.append(combination.copy())

                combination.pop()
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


        