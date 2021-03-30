class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return false
        else:
            nums.sort()
            
            for i in range(len(nums)-1):
                if nums[i] ==nums[i+1]:
                    return 'true'
                elif i == len(nums)-1:
                    return 'false'

                
 class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            hashset[num] = True
        return False
