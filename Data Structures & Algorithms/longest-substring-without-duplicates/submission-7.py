class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, maxLength = 0, 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            maxLength = max(maxLength, len(seen))
        
        return maxLength


        seen = set()
        if len(s) <= 1:
            return len(s)
        
        left, right, maxLength = 0, 1, 1
        seen.add(s[left])
        while left < right < len(s):
            currentChar = s[right]
            if currentChar not in seen:
                seen.add(currentChar)
                maxLength = max(maxLength, len(seen))
            else:
                while s[left] != currentChar:
                    seen.remove(s[left])
                    left += 1
                maxLength = max(maxLength, len(seen))
                left += 1
            right += 1
                

        return maxLength