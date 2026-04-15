class TimeMap:

    def __init__(self):
        self.timeBasedKVStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeBasedKVStore:
            self.timeBasedKVStore[key] = []
        self.timeBasedKVStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        val = ""
        if key in self.timeBasedKVStore:
            timeBasedValues = self.timeBasedKVStore[key]
            left, right = 0, len(timeBasedValues) - 1
            while left <= right:
                mid = (left + right) // 2
                midVal = timeBasedValues[mid]
                if midVal[0] == timestamp:
                    val = midVal[1]
                    break
                elif midVal[0] < timestamp:
                    val = midVal[1]
                    left = mid + 1
                else:
                    right = mid - 1
        
        return val
        
