from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True


# -------- Input Handling with prompts --------
m, n = map(int, input("Enter rows and columns (m n): ").split())

mat = []
print("Enter matrix rows:")
for _ in range(m):
    mat.append(list(map(int, input("Enter row: ").split())))

k = int(input("Enter k: "))

# -------- Call Solution --------
obj = Solution()
print("Result:", obj.areSimilar(mat, k))


# 2 3
# 1 2 3
# 1 2 3
# 3
# -> True