"""
Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

"""

# Python 3: Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def mergeInterval(self, intervals):

        if len(intervals) == 0:
            return []
        #Input: [[1,3],[2,6],[8,10],[15,18]]
        #Output: [[1,6],[8,10],[15,18]]
        
        intervals = sorted(intervals, key = lambda x: x.start)
        
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= res[-1].end: 
                res[-1].end = max(interval.end, res[-1].end)
            else: res.append(interval)
        return res
    