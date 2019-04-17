# Problem: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Solution 1: Convert to string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x_reverse = int(str(abs(x))[::-1])
            if x - x_reverse == 0:
                return True
            else:
                return False
                
# Solution 1
class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            temp = x
            y = 0
            while temp > 0:
                y = y * 10 + temp % 10
                temp = (temp - temp % 10) / 10
            return y == x

# Solution 2
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 ==0 and x != 0):
            return False
        else:
            y = 0
            while x > y:
                y = y * 10 + x % 10
                x = x/10
            return x == y or y/10 == x