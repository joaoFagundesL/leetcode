int findLengthOfLCIS(int* nums, int numsSize) {
    int max = 1, maxCurr = 1;

    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] < nums[i + 1]) {
            maxCurr++;
            if(maxCurr > max)
                max = maxCurr;
        } else         
            maxCurr = 1;
    }
    
    return max;
}
