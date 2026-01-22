from typing import List
from unittest import result


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [i] + digits
    
if __name__ == "__main__":
    n = int(input("Enter number of Digits: "))
    digits = list(map(int, input("Enter the Digits: ").split()))

    solution = Solution()
    result = solution.plusOne(digits)

    print("Result after plus one: ", result)


    # 3
    # 1 2 3
    # -> [1, 2, 4]