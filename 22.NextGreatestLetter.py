from typing import List
from unittest import result


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left % len(letters)]
    
if __name__ == "__main__":
    letters = input("Enter letters (space generated): ").split()
    target = input("Enter target characters: ").strip()
    solution = Solution()
    result = solution.nextGreatestLetter(letters, target)
    print("Output: ", result)

    # c f j
    # c
    # -> f