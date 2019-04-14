# Problem: You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels. The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Solution 1: Hash Table
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        hash_table = {}
        for i in range(len(J)):
            hash_table[J[i]] = i
        for j in range(len(S)):
            if S[j] in hash_table:
                count += 1
        return count 
            