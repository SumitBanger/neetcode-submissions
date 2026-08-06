class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        '''
        ### 2 Solutions are possible for this question ###
        1) Keep Hold of prevMax, prevMin till now + use both while figuring out currMax
            - Intution: 
                A) prevMax can turn to currMax in case current number is +ve
                B) prevMin can turn to currMax in case current number is -ve
        2) Keep Hold of prefix and suffix Product + Max of them would be currMax
            - Intution: (Think about all possible Cases)
                A) All numbers +ve -> Ans: Product of all numbers (prefixProd = suffixProd after loop)
                B) Even -ve numbers -> Ans: Product of all numbers (prefixProd = suffixProd after loop)
                C) Odd -ve numbers -> Ans: Skip one -ve number and Ans = Max(prefixProd, suffixProd) post all possible -ve number skips one by one
                D) In case of 0, reset prefixProd, suffixProd to 1 instead of 0
        '''
        # # Solution 1
        # result = prevMax = prevMin = nums[0]
        # for curr in nums[1:]:
        #     currMax = max(curr, curr*prevMax, curr*prevMin)
        #     currMin = min(curr, curr*prevMax, curr*prevMin)
        #     prevMax, prevMin = currMax, currMin
        #     result = max(result, currMax)
        # return result

        prefix = suffix = 1
        result = -11
        for i in range(len(nums)):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1
            prefix *= nums[i]
            suffix *= nums[len(nums) - i -1]
            result = max(result, prefix, suffix)
        return result

        