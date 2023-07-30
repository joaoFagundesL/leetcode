int search(int* nums, int numsSize, int target){
    int start = 0;
    int end = numsSize - 1;

    while(start <= end) {
        int mid = start + ((end - start) / 2);
        if(nums[mid] == target) return mid;
        if(target > nums[mid]) start = mid + 1;
        else end = mid - 1;
    }

    return -1;
}
