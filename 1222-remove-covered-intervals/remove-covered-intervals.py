class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[0] , -x[1]))
        removed = 0
        curr_end = 0
        for start, end in intervals:
            if end <= curr_end:
                removed += 1
            
            else:
                curr_end = end
            
        return (len(intervals) - removed)


        