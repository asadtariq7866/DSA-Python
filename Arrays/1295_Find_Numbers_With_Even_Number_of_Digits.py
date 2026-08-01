"""
LeetCode: 1295
Title: Find Numbers with Even Number of Digits

Pattern:
- Array Traversal
- Counting Digits

Time Complexity: O(n)

Space Complexity: O(1)
"""

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for num in nums:
            digits = len(str(num))

            if digits % 2 == 0:
                count += 1

        return count