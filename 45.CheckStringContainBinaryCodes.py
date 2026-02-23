class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False
        
        needed = 1 << k
        seen = set()

        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)

            if len(seen) == needed:
                return True
        
        return len(seen) == needed


if __name__ == "__main__":
    s = input("Enter binary string: ")
    k = int(input("Enter value of k: "))

    sol = Solution()
    result = sol.hasAllCodes(s, k)

    print("Output:", result)

    # 0010110
    # 2
    # -> True