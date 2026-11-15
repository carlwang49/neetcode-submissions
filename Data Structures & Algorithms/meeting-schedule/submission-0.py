"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals by start time
        sorted_intervals = sorted(intervals, key=lambda item: item.start)
        for i in range(len(sorted_intervals)):
            if i < len(sorted_intervals) - 1:
                if sorted_intervals[i].end > sorted_intervals[i+1].start:
                    return False
        return True

        