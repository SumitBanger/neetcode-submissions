class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countFreq_T, countFreq_S = {}, {}
        left, right, match, minLenSubstring = 0, 0, 0, ""

        for char in t:
            countFreq_T[char] = countFreq_T.get(char, 0) + 1
        
        while right < len(s): 
            currentChar = s[right]
            countFreq_S[currentChar] = countFreq_S.get(currentChar, 0) + 1
            if currentChar in countFreq_T and countFreq_S[currentChar] <= countFreq_T[currentChar]:
                match += 1

            if match == len(t):
                leftChar = s[left]
                while (leftChar not in countFreq_T) or (countFreq_S[leftChar] > countFreq_T[leftChar]):
                    countFreq_S[leftChar] -= 1
                    left += 1
                    leftChar = s[left]
                currentMinLengthStr = s[left:right+1]
                if minLenSubstring == "" or len(currentMinLengthStr) < len(minLenSubstring):
                    minLenSubstring = currentMinLengthStr    
            
            right += 1
            
        return minLenSubstring