class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        count = 0
        
        for num in range(left, right + 1):
            set_bits = num.bit_count()
            if isPrime(set_bits):
                count += 1
        
        return count


if __name__ == "__main__":
    left = int(input("Enter left: "))
    right = int(input("Enter right: "))
    sol = Solution()
    print("Output:", sol.countPrimeSetBits(left, right))


    # 6
    # 10
    # -> 4