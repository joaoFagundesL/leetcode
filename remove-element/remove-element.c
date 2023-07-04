/*
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
*/
int removeElement(int* nums, int numsSize, int val) {

    if(numsSize == 0) return 0;

    int i = 0, j = numsSize - 1;
    int aux;

    while(i != j) {
        if(nums[i] == val) {
            if(nums[j] == val)
                j--;
            else {
                nums[i] = nums[j];
                nums[j] = val;
            }
        } else
            i++;
    }

    for(int i = 0; i < numsSize; i++) {
        if(nums[i] == val) {
            aux = i;
            break;
        }
    }

    return aux;
}

/*

Another solution (similar to the one that removes duplicates from sorted array

int removeElement(int* nums, int numsSize, int val) {

    int j = 0;
    for(int i = 0; i < numsSize; i++) {
        if(nums[i] != val) {
            nums[j] = nums[i];
            j++;
        }
    }

    return j;
}

*/
