class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        tStringFrequency, sStringFrequency = {}, {}
        for char in t:
            tStringFrequency[char] = tStringFrequency.get(char, 0) + 1

        left, right, have, need = 0, 0, 0, len(tStringFrequency)
        res, resLen = [-1, -1], float("inf")
        current_have = 0
        
        for right in range(len(s)):
            char = s[right]
            sStringFrequency[char] = sStringFrequency.get(char, 0) + 1
            
            if char in tStringFrequency and sStringFrequency[char] == tStringFrequency[char]:
                current_have += 1
            
            while current_have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                
                sStringFrequency[s[left]] -= 1
                if s[left] in tStringFrequency and sStringFrequency[s[left]] < tStringFrequency[s[left]]:
                    current_have -= 1
                left += 1

        return "" if resLen == float("inf") else s[res[0] : res[1] + 1]