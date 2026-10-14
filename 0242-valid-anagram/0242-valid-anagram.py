class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        scount = {}
        for i in s:
            scount[i] = scount.get(i,0)+1
        for i in t:
            scount[i] = scount.get(i,0)-1
        for i in scount.values():
            if i != 0:
                return False
        return True