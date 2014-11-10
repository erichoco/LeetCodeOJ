#/usr/local/env python

# Problem link: https://oj.leetcode.com/problems/merge-intervals/

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
            return "["+str(self.start)+","+str(self.end)+"]"

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        merged = []
        for inter in intervals:
            overlapped = []
            for m in merged:
                if self.checkMerge(m, inter):
                    overlapped.append(m)
            if 0 == len(overlapped):
                merged.append(inter)
            else:
                for o in overlapped:
                    merged.remove(o)
                overlapped.append(inter)
                start = min([o.start for o in overlapped])
                end = max([o.end for o in overlapped])
                merged.append(Interval(start, end))
        return merged

    def checkMerge(self, inter1, inter2):
        if inter2.start > inter1.end or inter2.end < inter1.start:
            return False
        return True

def main():
    intervals = [Interval(2,4),Interval(3,5),Interval(1,10),Interval(11,12)]
    sol = Solution()
    print sol.merge(intervals)

if __name__ == "__main__":
    main()
