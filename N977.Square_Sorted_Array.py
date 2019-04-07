# Problem: Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Solution 1: Sort
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
        
# Time Complexity: O(nlog(n)); Space Complexity: O(n)