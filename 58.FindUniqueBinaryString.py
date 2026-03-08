from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('1' if x[i] == '0' else '0' for i, x in enumerate(nums))

# input
n = int(input("Enter number of binary strings: "))

nums = []
for i in range(n):
    nums.append(input("Enter binary string: ").strip())

# solve
obj = Solution()
result = obj.findDifferentBinaryString(nums)

print("Output:", result)

# 3
# 010
# 111
# 000
# -> 101
