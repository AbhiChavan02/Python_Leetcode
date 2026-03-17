class Solution:
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        res = 0

        # Build heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # Sort rows and calculate max area
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                res = max(res, matrix[i][j] * (j + 1))

        return res


# ===== INPUT SECTION =====
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter matrix row by row (space-separated 0/1):")
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)


# ===== EXECUTION =====
obj = Solution()
result = obj.largestSubmatrix(matrix)

print("Largest Submatrix Area:", result)


# 3
# 3
# 0 0 1
# 1 1 1
# 1 0 1
# -> 4