class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;

        for (int i = 0; i < k; i++) 
            sum += nums[i];

        double avg = sum / k , max = avg;
        int end = k, start = 0;

        while (end < nums.length) {
            sum += nums[end];   
            sum -= nums[start];

            avg = sum / k;

            if (avg > max) 
                max = avg;

            start++;
            end++;
        }

        return max;
    }
}