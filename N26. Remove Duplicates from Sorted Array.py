# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Solution: Double Pointers
class Solution(object):
    def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
        if len(nums) == 0:
            return 0
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                cur = cur + 1
                nums[cur] = nums[i]
        return cur + 1