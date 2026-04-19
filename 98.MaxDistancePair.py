from typing import List

class Solution:
    def maxDistance(self, A: List[int], B: List[int]) -> int:
        i, j = 0, 1

        while i < len(A) and j < len(B):
            if A[i] > B[j]:
                i += 1
            else:
                j += 1

        return j - i - 1


print("Enter array A (space separated):")
A = list(map(int, input().split()))
print("Enter array B (space separated):")
B = list(map(int, input().split()))

sol = Solution()
result = sol.maxDistance(A, B)

print("Output:", result)

# 30 29 19 5
# 25 25 25 25 25
# -> 2