class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0 for j in range(len(nums))]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            runningSum[i] = sum
        return runningSum