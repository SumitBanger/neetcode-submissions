class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        deq = collections.deque()
        res = []

        while right < len(nums):
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            deq.append(right)

            if (right - left + 1) >= k:
                res.append(nums[deq[0]])
                left += 1
                if left > deq[0]:
                    deq.popleft()

            right += 1
        
        return res