from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    sol = Solution()
    result = sol.sortByBits(arr)
    print("Sorted Array:", result)


    # 1 2 3 4 5 6 7 8
    # -> [1, 2, 3, 4, 5, 6, 7]