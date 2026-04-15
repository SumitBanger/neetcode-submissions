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

        
        # 2nd Approach (my original idea)
        if not s:
            return 0
        seen = {}
        seen[s[0]] = 0
        maxLength, start, prevMax = 1, 0, 1
        for i in range(1, len(s)):
            if s[i] not in seen or seen[s[i]] == -1:
                seen[s[i]] = i
                maxLength += 1
                prevMax = max(prevMax, maxLength)
            else:
                position = seen[s[i]]
                while start <= position:
                    seen[s[start]] = -1
                    start += 1
                    maxLength -= 1
                seen[s[i]] = i
                maxLength += 1
                prevMax = max(prevMax, maxLength)
        
        return prevMax