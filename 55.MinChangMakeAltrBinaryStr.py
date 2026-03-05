class Solution:
    def minOperations(self, s: str) -> int:
        c, j, n = 0, 0, len(s)
        for ch in s:
            if int(ch) == j:
                c += 1
            j ^= 1
        return min(c, n - c)


# take input from user
s = input("Enter binary string: ")

# create object
obj = Solution()

# call function and print result
result = obj.minOperations(s)
print("Minimum operations:", result)


# 0100
# -> 1