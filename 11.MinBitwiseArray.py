from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            found = -1
            for x in range(n + 1):
                if (x | (x + 1)) == n:
                    found = x
                    break
            ans.append(found)

        return ans


if __name__ == "__main__":
    nums = list(map(int, input("Enter nums array: ").split()))
    sol = Solution()
    print("Output:", sol.minBitwiseArray(nums))
