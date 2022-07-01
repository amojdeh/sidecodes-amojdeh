class Solution:
    def toHex(self, num: int) -> str:
        chars = '0123456789abcdef'
        ret = []
        if num < 0:
           num = math.pow(2, 32) - abs(num)
        while num > 0:
           ch = chars[int(num % 16)]
           ret.insert(0, ch)
           num //= 16
        return ''.join(ret) or '0'