class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, frequency, frequencyToNumsMap = [], {}, {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)     
        
        for num, numFrequency in frequency.items():
            if numFrequency in frequencyToNumsMap:
                frequencyToNumsMap[numFrequency].append(num)
            else:
                frequencyToNumsMap[numFrequency] = [num]

        totLength = len(nums)
        for i in range(totLength):
            currentFreq = totLength - i
            if currentFreq in frequencyToNumsMap:
                res.extend(frequencyToNumsMap[currentFreq])
                if len(res) >= k:
                    break

        return res[0:k]

        


        res, frequency = [], {}
        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)

        heap_items  = [(-value, key) for key, value in frequency.items()]

        # Convert into a max-heap by inverting values  
        #max_heap = [-n for n in nums]  
        heapq.heapify(heap_items)
        for i in range(0, k):
            value, key = heapq.heappop(heap_items)
            res.append(key)
        
        return res