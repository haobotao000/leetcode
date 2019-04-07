# Problem: Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Solution 1: Brute Force
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:(j+1)]) == k:
                    count += 1
        return count
        
# Time complexity: O(n^3); Space complexity: O(1)

# Solution 2: Brute Force with Prefix Sum
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            prefix_sum = 0
            for j in range(i, len(nums)):
                prefix_sum += nums[j]
                if prefix_sum == k:
                    count += 1
        return count 
            
    