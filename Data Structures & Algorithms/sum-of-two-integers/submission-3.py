class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 邏輯是不進位的處理加上進位的數字

        mask = 0xffffffff
        max_int = 0x7fffffff
        while b != 0: # b == 0 為終止條件，意思是沒有進位需要加上去了
            sum_without_carry = (a ^ b) & mask # 不進位
            carry = ((a & b) << 1) & mask # 進位
            
            a = sum_without_carry
            b = carry

        return a if a <= max_int else -((~a & mask) + 1)