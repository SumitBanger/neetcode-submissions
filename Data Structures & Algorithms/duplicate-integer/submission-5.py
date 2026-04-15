class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySeen = set()

        for num in nums:
            if num in alreadySeen:
                return True
            alreadySeen.add(num)
        return False
        
        
        
        return len(set(nums)) != len(nums)
        
        
        
        
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False