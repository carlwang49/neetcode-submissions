class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        remain_intervals = []
        for interval in sorted_intervals:
            if remain_intervals:
                if remain_intervals[-1][1] <= interval[0]:
                    remain_intervals.append(interval)
            else:
                remain_intervals.append(interval)
            
        return len(sorted_intervals) - len(remain_intervals)