import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelectSoln(nums, k - 1)
        heapq.heapify_max(nums)
        for _ in range(k):
            temp = heapq.heappop_max(nums)
        return temp
        
    def quickSelectSoln(self, nums, k):
        self.selection(0, len(nums) - 1, nums, k)
        return nums[k]

    def selection(self, left, right, nums, k):
        if left >= right: return
        pivot_idx = self.partition(left, right, nums, k)
        if pivot_idx == k:
            return
        elif pivot_idx > k:
            self.selection(left, pivot_idx - 1, nums, k)
        else:
            self.selection(pivot_idx + 1, right, nums, k)

    def partition(self, left, right, nums, k):
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        for index in range(left, right):
            if nums[index] > pivot:
                nums[index], nums[store_idx] = nums[store_idx], nums[index]
                store_idx += 1
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        return store_idx


