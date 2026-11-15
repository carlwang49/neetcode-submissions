class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        # res = x * x^4 * x^8 
        # x^2 -> x^4 -> x^8 
        while power: 
            if power & 1: # 奇數 x^13 = (x ^ 2 )^6 * x^1
                res *= x
            x *= x
            power = power // 2 # 6 -> 3 -> 1

        return res if n >= 0 else 1 / res