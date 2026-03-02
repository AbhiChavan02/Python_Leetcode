class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        zeros = []

        # Count trailing zeros in each row
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        swaps = 0

        for i in range(n):
            needed = n - i - 1
            j = i

            while j < n and zeros[j] < needed:
                j += 1

            if j == n:
                return -1

            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1
                swaps += 1

        return swaps


# --------- INPUT SECTION ----------
if __name__ == "__main__":
    n = int(input("Enter grid size (n): "))

    grid = []
    print("Enter grid rows (space separated 0/1 values):")
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    obj = Solution()
    result = obj.minSwaps(grid)

    print("Minimum swaps required:", result)


    # 3
    # 0 0 1
    # 1 1 0
    # 1 0 0
    # -> 3