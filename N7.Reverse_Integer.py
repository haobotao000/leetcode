# Problem: Given a 32-bit signed integer, reverse digits of an integer. Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Solution 1: 
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sign = 1
        else:
            sign = -1
        reverse = sign * int(str(abs(x))[::-1]) 
        if -(2 ** 31)-1 < reverse < (2 ** 31):
            return reverse
        else:
            return 0