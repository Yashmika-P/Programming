class Solution:
    def isHappy(self, n: int) -> bool:
        if n<0:
            return False
        s = set()
        while n!=1:
            sum = 0
            while n!= 0 :
                sum += (n%10)**2
                n //= 10
            if sum in s:
                return False
            s.add(sum)
            n = sum
        return True

        