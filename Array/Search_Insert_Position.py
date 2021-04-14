class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        start = 0
        end = len(nums)-1
        while start+1<end:
            mid = (start+end)/2
            if nums[mid]>target:
                end = mid
            else:
                start = mid
        
        if nums[start]>=target:
            return start
        if nums[end]>=target:
            return end
        return len(nums) 
