from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1] #problem asks for 1-indexed output
            elif two_sum < target:
                left += 1
            else:
                right -= 1
        return []
        
        