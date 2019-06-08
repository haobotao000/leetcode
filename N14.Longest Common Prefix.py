# Problem: Write a function to find the longest common prefix string amongst an array of strings.

# Solution 1: Brute Force
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            strs.sort()
            if strs[0] == "":
                return ""
        else:
            return ""
        for index, value in enumerate(strs[0]):
            for s in strs[1:]:
                if value != s[index]:
                    return strs[0][:index]
        return strs[0]

