class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        scount = {}
        tcount = {}

        for i in range(len(s)):
            # Count frequency of characters in both strings
            scount[s[i]] = scount.get(s[i], 0) + 1
            tcount[t[i]] = tcount.get(t[i], 0) + 1

        # Both strings are anagrams if frequencies match
        return scount == tcount