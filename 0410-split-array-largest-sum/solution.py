class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(minimum) -> bool:
            count = 1
            currSum = 0
            for num in nums:
                if currSum + num <= minimum:
                    currSum+=num
                else:
                    count+=1
                    currSum = num
            
            return count<=k

        l = max(nums)
        r = sum(nums)
        minimum = float(inf)
        while l <= r:
            m = l + (r-l)//2
            if canSplit(m):
                minimum = m
                r = m-1
            else:
                l = m+1
        
        return minimum
            
            

