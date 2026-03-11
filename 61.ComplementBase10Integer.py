class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        bit_length = n.bit_length()
        mask = (1 << bit_length) - 1
        return n ^ mask

n = int(input("Enter number: "))

obj = Solution()
result = obj.bitwiseComplement(n)

print("Complement:", result)


# 5
# -> 2