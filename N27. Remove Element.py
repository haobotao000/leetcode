# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Solution: Two pointers:
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cur] = nums[i]
                cur += 1
        return cur

