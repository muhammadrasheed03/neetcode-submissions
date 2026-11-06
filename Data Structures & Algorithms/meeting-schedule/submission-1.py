"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        ordered = sorted(intervals, key=lambda meeting: meeting.start)

        for i in range(1, len(ordered)):
            if ordered[i-1].end > ordered[i].start:
                return False
        return True