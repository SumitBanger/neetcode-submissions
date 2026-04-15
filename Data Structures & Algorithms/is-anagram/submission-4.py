class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charFrequency = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            charFrequency[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            charFrequency[index] -= 1
        
        if set(charFrequency) == {0}:
            return True
        return False

        
        
        if len(s) != len(t):
            return False
        frequencyS, frequencyT = {}, {}
        for c in s:
            frequencyS[c] = frequencyS.get(c,0) + 1
        
        for c in t:
            frequencyT[c] = frequencyT.get(c,0) + 1

        for c in frequencyS:
            if frequencyS[c] != frequencyT.get(c,0):
                return False
            
        return True
        
        return frequencyS == frequencyT