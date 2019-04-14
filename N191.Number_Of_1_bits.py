# Problem: Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

# Solution 1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        string = bin(n)[2:]
        for bit in string:
            if bit == '1':
                count += 1
        return count

# Solution 2
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')