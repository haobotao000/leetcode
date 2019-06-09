# Problem: Write a function to find the longest common prefix string amongst an array of strings.

# Solution 1: Brute Force (with sorting)
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

# Solution 2: Brute Force (without sorting)
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        ans = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return ans
            ans += strs[0][i]
        return strs[0]

