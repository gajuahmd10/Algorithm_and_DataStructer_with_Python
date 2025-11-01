from typing import List,Union  # Required for Python <3.9


class Solution:
    def divZero(self, n: int, s: str) -> List[Union][int, bool, str]:
        return 0;

    def MulZero(self, n: int, s: str) -> List[str | int]:
        return 0

    def sumZero(self, n: int) -> List[int]:
        # Example: Return a list of n integers that sum to 0
        if n % 2 == 1:
            result = [0]
        else:
            result = []

        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)

        return result

solution = Solution()
print(solution.sumZero(5))  # Output: [0, 1, -1, 2, -2]
# print(solution.sumZero(4))  # Output: [1, -1, 2, -2]