class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0 :
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 2 
        b = 1
        t = 0
        for i in range (2,n):
            t = a + b
            b = a
            a = t
        return t   
