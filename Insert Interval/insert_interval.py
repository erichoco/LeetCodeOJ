#/usr/local/env python

# Problem link: https://oj.leetcode.com/problems/insert-interval/

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
            return "["+str(self.start)+","+str(self.end)+"]"

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if 0 == len(intervals):
            return [newInterval]
        mergeStartIdx, mergeEndIdx = None, None
        for idx, inter in enumerate(intervals):
            if newInterval.start < inter.start:
                if 0 < idx and newInterval.start <= intervals[idx-1].end:
                    mergeStartIdx = idx-1
                else:
                    mergeStartIdx = idx
                break
        else:
            mergeStartIdx = len(intervals)
            if newInterval.start <= intervals[len(intervals)-1].end:
                mergeStartIdx -= 1
        intervals.insert(mergeStartIdx, newInterval)
        for idx, inter in enumerate(intervals[mergeStartIdx:]):
            idx = mergeStartIdx + idx
            if newInterval.end < inter.start:
                mergeEndIdx = idx
                break
        else:
            mergeEndIdx = len(intervals)
        intervals = intervals[:mergeStartIdx] \
                  + self.merge(intervals[mergeStartIdx:mergeEndIdx]) \
                  + intervals[mergeEndIdx:]
        return intervals

    def merge(self, intervals):
        if len(intervals):
            return [Interval(min([i.start for i in intervals]),
                                    max([i.end for i in intervals]))]
        return []


def main():
    # intervals = [Interval(2,4),Interval(5,6),Interval(9,13),Interval(15,20)]
    intervals = [Interval(1,5)]
    sol = Solution()
    print sol.insert(intervals, Interval(2,3))

if __name__ == "__main__":
    main()

