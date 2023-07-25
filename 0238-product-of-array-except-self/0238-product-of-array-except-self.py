from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #length of input list
        length = len(nums)
        
        answer= [0]*length
        
        #answer[i] is initially the product of all numbers to the left of i
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            
        # R contains the product of all numbers to the right of i
        R = 1
        for i in reversed(range(length)):
            # For the index i, answer[i] contains the product of all numbers to the left and R would contain the product of all numbers to the right.
            # We update answer[i] with the product of answer[i] and R
            answer[i] = answer[i] * R
            
            # R contains the product of all numbers to the right. We update R accordingly
            R *= nums[i]
            
        return answer