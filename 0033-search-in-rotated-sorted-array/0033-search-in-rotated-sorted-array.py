from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            #when the left half [left, mid] is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    #target lies in the sorted left half
                    right = mid - 1
                else:
                    #target lies in the right half
                    left = mid + 1
            else:
                #when the right half [mid, right] is sorted
                if nums[mid] <= target <= nums[right]:
                    #target lies in the sorted right half
                    left = mid + 1
                else:
                    #target lies in the left half
                    right = mid - 1

        #target was not found in the array
        return -1


