class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            distinct = 0
            maxFreq = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')

                if freq[idx] == 0:
                    distinct += 1

                freq[idx] += 1
                maxFreq = max(maxFreq, freq[idx])

                length = j - i + 1

                if length == distinct * maxFreq:
                    ans = max(ans, length)

        return ans


# -------- Main Function --------
if __name__ == "__main__":
    s = input("Enter string: ")
    sol = Solution()
    result = sol.longestBalanced(s)
    print("Longest Balanced Substring Length:", result)


# abbac
# -> 4