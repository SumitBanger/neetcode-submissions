class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elementsMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in elementsMap:
                diffIndex = elementsMap[diff]
                return [diffIndex, index]
            if num not in elementsMap:
                elementsMap[num] = index



        