class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, maxLength = 0, 0, 0
        count = {}
        while left <= right and right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            right += 1
            maxCharFreq = max(count.values())
            currentWindowSize = right - left
            if currentWindowSize - maxCharFreq <= k:
                maxLength = max(maxLength, currentWindowSize)
            else:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
        
        return maxLength

