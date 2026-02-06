from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        l = 0
        max_len = 1

        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            max_len = max(max_len, r - l + 1)

        return n - max_len
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter Array elements (space separated): ").split()))
    k = int(input("Enter k: "))

    solution = Solution()
    print("Minimum removals: ", solution.minRemoval(nums, k))


    # 2 1 5
    # 2
    # -> 1