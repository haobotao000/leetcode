# Problem: Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
# Solution 1:
class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for letter in str:
            if ord('A') <= ord(letter) <= ord('Z'):
                ans += chr(ord(letter) - ord('A') + ord('a'))
            else:
                ans += letter
        return ans