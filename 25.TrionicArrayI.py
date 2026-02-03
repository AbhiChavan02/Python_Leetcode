from typing import List

class Solution:
    def isTrionicI(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        if i == 0:
            return False
        p = i

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        if i == p:
            return False
        q = i

        if q == n - 1:
            return False
        
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements separated by space: ").split()))

    solution = Solution()
    result = solution.isTrionicI(nums)
    print("Output: ", result)


    # 1 3 5 4 2 6
    # -> True

    # 3 7 1 
    # -> False

    # 3 7 1 2
    # -> True