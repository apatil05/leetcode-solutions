class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binSearch(nums, target, leftBias):

            l,r = 0, len(nums) - 1
            res = -1
            while l<=r:
                m = l + (r-l)//2
                
                if nums[m] == target:
                    res = m
                    if leftBias:
                        r = m-1
                    else:
                        l = m+1
                elif target > nums[m]:
                    l = m+1
                else:
                    r = m - 1
        
            return res
        
        left = binSearch(nums,target,True)
        right = binSearch(nums, target, False)

        return [left, right]
                    

