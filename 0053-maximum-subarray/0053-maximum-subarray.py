class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        subsum = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            subsum = max(subsum+nums[i], nums[i])
            maxsum = max(maxsum,subsum)
        return maxsum

        