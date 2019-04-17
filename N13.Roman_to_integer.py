# Problem: 

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        leng = len(s)
        integer = 0
        for i in range(leng - 1):
            if roman[s[i]] < roman[s[i+1]]:
                integer -= roman[s[i]]
            else:
                integer += roman[s[i]]
        return integer + roman[s[leng - 1]]
            
