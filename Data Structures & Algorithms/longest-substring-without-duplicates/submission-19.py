class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # maps character -> its most recent index
        longest_till_now = 0
        left = 0
        
        for right, char in enumerate(s):
            # If the character is inside the current window, jump the left pointer
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            char_map[char] = right
            longest_till_now = max(longest_till_now, right - left + 1)
            
        return longest_till_now

        # seen, longestTillNow, left = set(), 0, 0
        # for char in s:
        #     while char in seen:
        #         seen.remove(s[left])
        #         left += 1
        #     seen.add(char)
        #     longestTillNow = max(longestTillNow, len(seen))
        # return longestTillNow

        # My Original Idea
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