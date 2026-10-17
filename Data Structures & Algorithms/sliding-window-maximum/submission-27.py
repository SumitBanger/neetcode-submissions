class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxTillNow_DQ, left, result = collections.deque(), 0, []

        for right, num in enumerate(nums):
            while maxTillNow_DQ and num >= nums[maxTillNow_DQ[-1]]:
                maxTillNow_DQ.pop()
            maxTillNow_DQ.append(right)

            if right >= k-1:
                result.append(nums[maxTillNow_DQ[0]])
                if left == maxTillNow_DQ[0]:
                    maxTillNow_DQ.popleft()
                left += 1

        # for index, num in enumerate(nums[0:k]):
        #     while maxTillNow_DQ and num >= maxTillNow_DQ[-1][1]:
        #         maxTillNow_DQ.pop()
        #     maxTillNow_DQ.append((index, num))
        
        # result.append(maxTillNow_DQ[0][1])
        # for right in range(k, len(nums)):
        #     if left == maxTillNow_DQ[0][0]:
        #         maxTillNow_DQ.popleft()
        #     left += 1

        #     num = nums[right]
        #     while maxTillNow_DQ and num >= maxTillNow_DQ[-1][1]:
        #         maxTillNow_DQ.pop()
        #     maxTillNow_DQ.append((right, num))
            
        #     result.append(maxTillNow_DQ[0][1])
            
        return result


        

        