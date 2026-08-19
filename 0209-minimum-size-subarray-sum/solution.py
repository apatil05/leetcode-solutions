import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if len(nums) == 1 and nums[0] < target:
            return 0
        
        
        minWindow = math.inf
        l = 0
        s = nums[0]
        if s>=target:
            return 1
        for r in range(1,len(nums)):
            s += nums[r]
            while s >= target:
                windowSize = r-l + 1
                minWindow = min(windowSize, minWindow)
                s-=nums[l]
                l+=1

        return minWindow if minWindow != math.inf else 0

                

