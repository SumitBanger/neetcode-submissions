class MedianFinder:

    def __init__(self):
        self.lowerMaxHeap, self.upperMinHeap = [], []  

    def addNum(self, num: int) -> None:
        if len(self.lowerMaxHeap) - len(self.upperMinHeap) >= 0:
            heapq.heappush(self.upperMinHeap, num)
        else:
            heapq.heappush_max(self.lowerMaxHeap, num)

        if len(self.lowerMaxHeap) - len(self.upperMinHeap) >= 0 and self.upperMinHeap and self.lowerMaxHeap[0] > self.upperMinHeap[0]:
            heapq.heappush(self.upperMinHeap, heapq.heappop_max(self.lowerMaxHeap))
        elif len(self.upperMinHeap) - len(self.lowerMaxHeap) >= 0 and self.lowerMaxHeap and self.upperMinHeap[0] < self.lowerMaxHeap[0]:
            heapq.heappush_max(self.lowerMaxHeap, heapq.heappop(self.upperMinHeap))

        if len(self.lowerMaxHeap) - len(self.upperMinHeap) > 1:
            heapq.heappush(self.upperMinHeap, heapq.heappop_max(self.lowerMaxHeap))
        elif len(self.upperMinHeap) - len(self.lowerMaxHeap) > 1:
            heapq.heappush_max(self.lowerMaxHeap, heapq.heappop(self.upperMinHeap))
        
    def findMedian(self) -> float:
        if len(self.lowerMaxHeap) - len(self.upperMinHeap) == 1:
            return self.lowerMaxHeap[0]
        elif len(self.upperMinHeap) - len(self.lowerMaxHeap) == 1:
            return self.upperMinHeap[0]
        else:
            return ((self.lowerMaxHeap[0] + self.upperMinHeap[0]) / 2)
        