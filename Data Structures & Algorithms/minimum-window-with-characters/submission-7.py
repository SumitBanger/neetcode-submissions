class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        tStringFrequency, sStringFrequency = {}, {}
        for char in t:
            tStringFrequency[char] = tStringFrequency.get(char, 0) + 1

        left, right, have, need = 0, 0, 0, len(tStringFrequency)
        res, resLen = [0, 0], 2000
        current_have = 0
        
        while right < len(s):
            rightChar = s[right]
            sStringFrequency[rightChar] = sStringFrequency.get(rightChar, 0) + 1
            if rightChar in tStringFrequency and sStringFrequency[rightChar] == tStringFrequency[rightChar]:
                current_have += 1

            while current_have == need:
                currentLength = right - left + 1
                if currentLength < resLen:
                    resLen = currentLength
                    res = [left, right]
                
                leftChar = s[left]
                sStringFrequency[leftChar] = sStringFrequency.get(leftChar, 0) - 1
                if leftChar in tStringFrequency and sStringFrequency[leftChar] < tStringFrequency[leftChar]:
                    current_have -= 1
                left += 1
            
            right += 1

        return "" if resLen == 2000 else s[res[0] : res[1] + 1]