class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        


        intervals.sort(key = lambda x: x[0])
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            currS, currE = intervals[i]
            stackS, stackE = stack[-1]

            if currS <= stackE:
                merged = [stackS, max(currE, stackE) ]
                stack.pop()
                stack.append(merged)
            else:
                stack.append(intervals[i])
            
        return stack

        

                
            
            

