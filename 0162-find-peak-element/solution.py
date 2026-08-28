import math
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Some implementation of binary search, but I think the key is how can we divide the input in half/ reduce our search in half each time
        #No sorting is allowed obv
        #Neighboring elements are guaranteed to be !=

        #O(N) approach would just be to iterate through arr and check left + right elements, then if condition is met return element

        #The number we are at is a peak
            #return
        #else
            #The number we are at is not a peak, which means that either the left or right number is greater (or both)
            #

        l,r = 0, len(nums) - 1

        if len(nums) == 1:
            return 0

        while l <= r:
            m = l + (r-l)//2
            if m == 0:
                ml = -math.inf
                mr = nums[m+1]
            elif m == len(nums) - 1:
                mr = -math.inf
                ml = nums[m-1]
            else:
                ml = nums[m-1]
                mr = nums[m+1]

            
            if nums[m] > ml and nums[m] > mr:
                return m
            elif mr > nums[m]:
                l = m + 1
            else:
                r = m-1

