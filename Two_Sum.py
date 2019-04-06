# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Solution 1: Brute force
def twoSum(nums, target):
    for i, num1 in enumerate(nums, start = 0):
        for j, num2 in enumerate(nums[i+1:], start = 1):
            if num1 + num2 == target:
                return i, j
                
# Time Complexity: O(n^2)
# Space Compexity: O(1)

# Solution 2: Two pass Hash Table

        