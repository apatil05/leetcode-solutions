class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l,r = 0, len(arr) -1 

        while l <= r:
            m = l + (r-l)//2

            ml, mr = arr[m-1], arr[m+1]
            if m == 0:
                ml = -math.inf
            
            if m == len(arr) - 1:
                mr = - math.inf
            
            if arr[m] > ml and arr[m] > mr:
                return m
            elif mr > arr[m]:
                l = m+1
            else:
                r = m-1
        

