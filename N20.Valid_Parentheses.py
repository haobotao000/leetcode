#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

# Solution 1: Slack
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        slack = ['a']
        # Build a dictionary
        par_map = {')':'(', ']':'[', '}':'{'} 
        for i in s:
            if i in par_map:
                if par_map[i] != slack.pop():
                    return False
            else:
                slack.append(i)
        return len(slack) == 1