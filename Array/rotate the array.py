class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        length = len(nums)
        k = k % length
        result = nums[length - k : length] + nums[:length - k]
        return result
