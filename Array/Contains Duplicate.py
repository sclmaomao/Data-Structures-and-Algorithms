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
