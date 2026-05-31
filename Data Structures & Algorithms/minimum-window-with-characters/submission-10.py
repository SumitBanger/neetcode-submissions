class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLenSubstring = ""
        # if len(t) > len(s):
        #     return minLenSubstring
        
        countFreq_T, countFreq_S = {}, {}

        for char in t:
            countFreq_T[char] = countFreq_T.get(char, 0) + 1

        left, right, match = 0, 0, 0
        while right < len(s): 
            currentChar = s[right]
            if currentChar in countFreq_T:
                countFreq_S[currentChar] = countFreq_S.get(currentChar, 0) + 1
                if countFreq_S[currentChar] <= countFreq_T[currentChar]:
                    match += 1

            if match == len(t):
                leftChar = s[left]
                while (leftChar not in countFreq_T) or (countFreq_S[leftChar] > countFreq_T[leftChar]):
                    if leftChar in countFreq_T:
                        countFreq_S[leftChar] -= 1
                    left += 1
                    leftChar = s[left]
                currentMinLengthStr = s[left:right+1]
                if minLenSubstring == "" or len(currentMinLengthStr) < len(minLenSubstring):
                    minLenSubstring = currentMinLengthStr    
            
            right += 1
            
        return minLenSubstring