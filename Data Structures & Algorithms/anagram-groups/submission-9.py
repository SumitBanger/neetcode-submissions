class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countToAnagramsMap = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                charIndex = ord(char) - ord('a')
                count[charIndex] += 1
            countToAnagramsMap[tuple(count)].append(string)
        
        return list(countToAnagramsMap.values())

        # Below Solution is using Frquency Tuples
        frequencyToStringsMap = {}
        for string in strs:
            frequencyTuple = self.getFrequencyMapTuple(string)
            if frequencyTuple not in frequencyToStringsMap:
                frequencyToStringsMap[frequencyTuple] = []
            frequencyToStringsMap[frequencyTuple].append(string)

        return list(frequencyToStringsMap.values())

    def getFrequencyMapTuple(self, string):
        frequency = {}
        for char in string:
            frequency[char] = frequency.get(char, 0) + 1
        return tuple(sorted(frequency.items()))
