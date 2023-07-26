int missingNumber(int* nums, int numsSize){
    int xorNums1 = 0;
    
    for(int i = 0; i < numsSize; i++) xorNums1 ^= nums[i];
    for(int i = 0; i < numsSize + 1; i++) xorNums1 ^= i;
    return xorNums1;
}
