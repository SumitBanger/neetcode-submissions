class TimeMap:

    def __init__(self):
        self.timeBasedKVStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key in self.timeBasedKVStore:
        self.timeBasedKVStore[key].append((timestamp, value))
        # else:
        #     self.timeBasedKVStore[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        val = ""
        if key in self.timeBasedKVStore:
            existingList = self.timeBasedKVStore[key]
            left, right = 0, len(existingList) - 1
            while left <= right:
                mid = (left + right) // 2
                midVal = existingList[mid]
                if timestamp == midVal[0]:
                    return midVal[1]
                elif timestamp > midVal[0]:
                    val = midVal[1]
                    left = mid + 1
                else:
                    right = mid - 1
        
        return val
        
