class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1, countS2, matching = [0] * 26, [0] * 26, 0
        for index in range(len(s1)):
            countS1[ord(s1[index]) - ord('a')] += 1
            countS2[ord(s2[index]) - ord('a')] += 1

        for index in range(26):
            if countS1[index] == countS2[index]:
                matching += 1

        if matching == 26:
            return True
        
        left, right = 0, len(s1) - 1
        while right < len(s2) - 1:
            countS2[ord(s2[left]) - ord('a')] -= 1
            if countS1[ord(s2[left]) - ord('a')] == countS2[ord(s2[left]) - ord('a')] + 1:
                matching -= 1
            elif countS1[ord(s2[left]) - ord('a')] == countS2[ord(s2[left]) - ord('a')]:
                matching += 1
            left +=1
            
            right += 1
            countS2[ord(s2[right]) - ord('a')] += 1
            if countS1[ord(s2[right]) - ord('a')] == countS2[ord(s2[right]) - ord('a')] - 1:
                matching -= 1
            elif countS1[ord(s2[right]) - ord('a')] == countS2[ord(s2[right]) - ord('a')]:
                matching += 1

            if matching == 26:
                return True
        
        return False
        
        # Below solution is using hashmap, above one uses list (little more complex but optimised)
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
