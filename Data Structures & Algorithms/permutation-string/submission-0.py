class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        frequencyS1, frequencyS2 = {}, {}
        for index in range(len(s1)):
            frequencyS1[s1[index]] = frequencyS1.get(s1[index], 0) + 1
            frequencyS2[s2[index]] = frequencyS2.get(s2[index], 0) + 1

        if frequencyS1 == frequencyS2:
            return True
        left, right = 0, len(s1) - 1
        while right < len(s2) - 1:
            frequencyS2[s2[left]] -= 1
            if frequencyS2[s2[left]] == 0:
                del frequencyS2[s2[left]]
            left += 1
            right += 1
            frequencyS2[s2[right]] = frequencyS2.get(s2[right], 0) + 1
            if frequencyS1 == frequencyS2:
                return True
            
        return False
