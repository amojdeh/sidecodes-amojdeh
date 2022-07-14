class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = [2,3,5,7,11,13,17,19]
        
        def count_bits(x):
            count = 0
            return bin(x).count('1')
        ans = 0
        for i in range(left, right + 1):
            if count_bits(i) in primes:
                ans += 1
        return ans