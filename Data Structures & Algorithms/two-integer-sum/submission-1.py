class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # Hashmap containing Number -> Index Mapping for all the already seen values
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index
        
        
        
        
        
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        