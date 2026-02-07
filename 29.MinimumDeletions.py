class Solution:
    def minimumDeletions(self, s: str) -> str:
        b_count = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)
            
        return deletions
    
s = input("Enter the string (only 'a' and 'b'): ")
solution = Solution()
print(solution.minimumDeletions(s))


# bbaaaaabb
# -> 2