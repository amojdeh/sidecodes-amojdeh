class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count_bits(x):
            return bin(x).count('1')
        
        primes = [2,3,5,7,11,13,17,19]
        count = 0
        for i in range(left, right + 1):
            if count_bits(i) in primes:
                count += 1
        return count