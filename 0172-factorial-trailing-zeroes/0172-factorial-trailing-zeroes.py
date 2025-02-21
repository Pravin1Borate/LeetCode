class Solution:
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n-1)
    
    def calculate_zeros(self,n):
        zero_count = 0
        while n % 10 == 0:
            zero_count += 1
            n = n // 10
        return zero_count


    def trailingZeroes(self, n: int) -> int:
        fact_number = self.factorial(n)
        zero_count  = self.calculate_zeros(fact_number)
        return zero_count