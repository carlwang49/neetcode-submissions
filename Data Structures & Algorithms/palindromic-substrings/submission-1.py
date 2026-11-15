class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    count += 1

        return count