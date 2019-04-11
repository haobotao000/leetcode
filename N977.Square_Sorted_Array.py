# Problem: Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Solution 1: Sort
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
        
# Time complexity: O(nlog(n)); Space complexity: O(n)

# Solution 2: Two Pointer
class Solution(object):
    def sortedSquares(self, A):
        j = 0
        N = len(A)
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        
        ans = []
        while 0 <= i and j < N:
            if A[i] ** 2 <= A[j] ** 2:
                ans.append(A[i] ** 2)
                i += -1
            else:
                ans.append(A[j] ** 2)
                j += 1
        while i >= 0:
            ans.append(A[i] ** 2)
            i += -1
        while j < N:
            ans.append(A[j] ** 2)
            j += 1
        return ans
# Time complexity: O(n); Space complexity: O(n)

# Solution 3: Two Pointer Revised
class Solution(object):
    def sortedSquares(self, A):
        ans = collections.deque()
        left, right = 0, len(A) - 1
        while left <= right:
            if A[left] ** 2 <= A[right] ** 2:
                ans.appendleft(A[right] ** 2)
                right -= 1
            else:
                ans.appendleft(A[left] ** 2)
                left += 1
        return list(ans)
                
                
                
                
                
                
                
                
                
                
  
         
