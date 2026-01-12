from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        write = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[write] = nums[i]
                write += 1

        return write
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))

    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Number of unique elements: ", k)
    print("Array after removing duplicates: ", nums[:k])


    # 0 0 0 2 3 4 5 6 6 7 7 7 8 8 -> 
    # Number of unique elements:  8, 
    # Array after removing duplicates:  [0, 2, 3, 4, 5, 6, 7, 8]