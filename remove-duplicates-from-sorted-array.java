class Solution {
    public int removeDuplicates(int[] nums) {

        /* It's like a pointer for the unique elements. I set as 1 because the element at
        the index 0 will be unique */

        /* [0, 1, 1, 1, 2] 
        *         ^---- unique pointer 
        *               ^---- different from its previous 
        * replace unique with the different one: [0, 1, 2, 1, 2] 
        * the first 3 elemets are unique [0, 1, 2]
        */

        /* I don't have to worry with the 0 index element. When I first find an element
        that is different from its previous I can modify the element where the pointer 'unique' is pointing*/

        int unique = 1;

        /* With -1 i assure that wont be invalid access, cuz im going until that last but one
        another possible solution would be to compare with its predecessor. i = 1 and nums[i] != nums[i - 1] */
        for(int i = 0; i < nums.length - 1; i++) {
            if(nums[i] != nums[i + 1]) {
                nums[unique] = nums[i + 1];
                unique++;
            }
        }

        return unique;
    }
}
