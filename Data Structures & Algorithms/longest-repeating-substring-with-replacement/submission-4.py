class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, maxLength = 0, 0, 0
        count = {}
        maxCharFreq = 0
        while left <= right and right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            if maxCharFreq < count[s[right]]:
                maxCharFreq = count[s[right]]
            right += 1
            #maxCharFreq = max(count.values())
            currentWindowSize = right - left
            if currentWindowSize - maxCharFreq <= k:
                maxLength = max(maxLength, currentWindowSize)
            else:
                if maxCharFreq == count[s[left]]:
                    maxCharFreq -= 1
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
        
        return maxLength

