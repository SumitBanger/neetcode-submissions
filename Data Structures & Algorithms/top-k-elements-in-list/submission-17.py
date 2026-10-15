class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqencyMap, result = Counter(nums), []    
        # invertedFreqencyMap = defaultdict(list)
        # for num, freq in freqencyMap.items():
        #     invertedFreqencyMap[freq].append(num)

        # itemsBucketList = [None] * len(nums)
        # for freq, numList in invertedFreqencyMap.items():
        #     itemsBucketList[freq - 1] = numList

        # for numList in reversed(itemsBucketList):
        #     if numList:
        #         if len(result) < k:
        #             result.extend(numList)
        #         else: 
        #             break
        
        # 2. Create buckets where index = frequency - O(N) space
        # Size is len(nums) + 1 to easily handle a max frequency equal to len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # 3. Populate buckets directly - O(N) time
        for num, freq in freqencyMap.items():
            buckets[freq].append(num)
                    
        # 4. Gather elements from highest to lowest frequency - O(N) time
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


        




        