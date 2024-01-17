class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(interval -> interval[1]));
        int interval_end = intervals[0][1];
        int remove = 0;

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < interval_end) 
                remove++;
            else 
                interval_end = intervals[i][1];
        }

        return remove;
    }
}
