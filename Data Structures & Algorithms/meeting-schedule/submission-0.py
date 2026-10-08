"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)

        for interval1, interval2 in zip(intervals, intervals[1:]):
            if interval1.end > interval2.start:
                return False
        return True
