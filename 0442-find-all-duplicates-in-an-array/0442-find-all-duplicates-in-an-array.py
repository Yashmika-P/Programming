class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num-1
            if nums[idx] < 0:
                l.append(num)
            nums[idx] = nums[idx]*-1
        return l