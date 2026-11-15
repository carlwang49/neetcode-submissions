class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1 if x >= 0 else -1
        x_str = str(abs(x))
        rev_str = ""
        for s in x_str:
            rev_str = s + rev_str
        rev = sign * int(rev_str)
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
