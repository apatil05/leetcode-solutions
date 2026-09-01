class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(m):
            count = 1
            currentSum = 0
            for num in nums:
                if currentSum + num <= m:
                    currentSum+=num
                else:
                    count+=1
                    currentSum = num
            
            return count <= k

        l,r = max(nums), sum(nums)
        minimum = float(inf)

        while l<=r:
            m = l + (r-l)//2

            if canSplit(m):
                r = m-1
                minimum = m
            else:
                l = m+1
        
        return minimum

