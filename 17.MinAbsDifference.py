from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result
    
if __name__ == "__main__":
    n = int(input("Enter Number of Elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    solution = Solution()
    ans = solution.minimumAbsDifference(arr)

    print("Minimum Absolute Difference Pairs: ")
    print(ans)

    # 4
    # 4 2 1 3
    # -> [[1, 2], [2, 3], [3, 4]]