class Solution:
    def findMin(self, nums: List[int]) -> int:
         # When array is of size 1 or not rotated at all.
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If mid is greater than mid + 1, then mid+1 is the smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # If mid is smaller than mid - 1, then mid is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # Move to the unsorted side of the array
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
