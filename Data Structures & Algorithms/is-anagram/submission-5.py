class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencyS, frequencyT = {}, {}
        for char in s:
            frequencyS[char] = frequencyS.get(char, 0) + 1
        for char in t:
            frequencyT[char] = frequencyT.get(char, 0) + 1

        if frequencyS == frequencyT:
            return True
        return False

        