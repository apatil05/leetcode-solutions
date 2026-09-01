class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        For each car: 
            1.) See where it starts compraed to target
            2.) calculate in how many hours it would reach
            3.) If a car that started further away catches up to a car that was in front they are added to the same fleet --> This is true even if they catch up at Target
                Substeps:
                We need the position of each car sorted descending, that way the cars that start closest to target come first
                Then we can calculate the rate of travel for each car, aka what hour they would reach the target
                We need to use a stack:

        """
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for car in cars:
            currP, currS = car
            currH = (target - currP) / currS
            if stack and currH <= stack[-1][2]:
                #Merge Cars:
                stackP, stackS, stackH = stack.pop()
                stack.append( (stackP, min(currS, stackS), max(currH, stackH)) )
            else:
                stack.append((currP, currS, currH))
    
        return len(stack)


        

