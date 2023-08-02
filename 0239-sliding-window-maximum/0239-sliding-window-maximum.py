from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        
        for i in range(len(nums)):
            #remove elements out of window
            
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            #remove all numbers smaller than current number from right to left
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            dq.append(i)
            
            #add into results
            if i >= k - 1:
                ans.append(nums[dq[0]])
                
        return ans