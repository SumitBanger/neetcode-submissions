class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqencyMap, result = {}, []
        for num in nums:
            freqencyMap[num] = freqencyMap.get(num, 0) + 1
        
        invertedFreqencyMap = defaultdict(list)
        for num, freq in freqencyMap.items():
            invertedFreqencyMap[freq].append(num)

        while len(result) < k:
            maxFreq = max(invertedFreqencyMap.keys())
            result.extend(invertedFreqencyMap[maxFreq])
            del invertedFreqencyMap[maxFreq]

        return result




        