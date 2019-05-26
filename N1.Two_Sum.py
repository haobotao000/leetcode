# Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Solution 1: Brute force
def twoSum(nums, target):
    for i, num1 in enumerate(nums[: (len(nums) - 1)], start = 0):
        for j, num2 in enumerate(nums[i+1:], start = 1):
            if num1 + num2 == target:
                return i, j
                
# Time Complexity: O(n^2)
# Space Compexity: O(1)

# Solution 2: Two pass Hash Table
def twoSum(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        hash_table[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            if hash_table[target - nums[i]] != i:
                return i, hash_table[target - nums[i]]
                

# Solution 3: One pass Hash Table
def twoSum(nums, target):
    hash_table = {}
    for i, num in enumerate(nums, start = 0):
        if target - num in hash_table:
            return hash_table[target - num], i
        hash_table[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)
        


        