class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using a single result array
        prefix, postfix, res = 1, 1, [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
           
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        
        
        productTillNow, frontPassList = 1, []
        for index in range(len(nums)):
            frontPassList.append(productTillNow)
            productTillNow *= nums[index]

        productTillNow, result = 1, [1] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            result[index] = productTillNow * frontPassList[index]
            productTillNow *= nums[index]
        
        return result

        