class Solution:
    def reverseBits(self, n: int) -> int:
        res_str = ''
        n_in_32bit = '0' * (32-len(bin(n)[2:])) + bin(n)[2:]
        for bit in n_in_32bit:
            res_str = bit + res_str
        return int(res_str, 2)