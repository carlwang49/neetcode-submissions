class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Transfer list to str
        digits_str = ''
        for d in digits:
            digits_str += str(d)
        digits_int = int(digits_str)
        return list(str(digits_int+1))