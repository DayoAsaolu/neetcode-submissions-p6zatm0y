"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start time 1st, then we look for overlap
        #  te[n-1] > ts[n] - overlap

        if len(intervals) <= 1: return True

        intervals = sorted(intervals, key=lambda t: t.start)
        print(intervals)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        
        return True