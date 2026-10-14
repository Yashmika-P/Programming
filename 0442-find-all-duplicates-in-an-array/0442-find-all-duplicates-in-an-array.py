class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h = {}
        l = []
        for i in nums:
            h[i] = h.get(i,0)+1
        for i in h:
            if h.get(i) == 2:
                l.append(i)
        return l
