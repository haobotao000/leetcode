# Problem: Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Solution 1: Hash Table
class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for i in range(len(nums)):
            try:
                 hash_table.pop(nums[i])
            except:
                 hash_table[nums[i]] = 1
        return hash_table.popitem()[0]
        
# nums = [4, 2, 4, 2, 3]; hash_table = {3:1}; hash_table.popitem() = (3, 1)
# Time complexity: O(n); Space complexity: O(n)

# Solution 2: Math
# use set() to get all the unique items.
class Solution(object):
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)

# Time complexity: O(n+n); Space complexity: O(n)