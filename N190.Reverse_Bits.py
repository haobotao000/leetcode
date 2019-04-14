# Problem: Reverse bits of a given 32 bits unsigned integer.
# Solution 1
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(format(n, "b").zfill(32)[::-1], 2)
        
# Solution 2
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)
 