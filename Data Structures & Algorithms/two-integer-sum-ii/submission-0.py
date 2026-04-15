class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]
            if currentSum < target:
                left += 1
            if currentSum > target:
                right -= 1
        return []