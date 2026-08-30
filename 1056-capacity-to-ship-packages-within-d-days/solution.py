class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(shipWeight):
            d = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight <= shipWeight:
                    currWeight += weight
                else:
                    d+=1
                    currWeight = weight

            return d<=days
            





        
        maxW = sum(weights)
        minW = max(weights)
        shipWeight = float(inf)

        while minW <= maxW:
            
            m = minW + (maxW - minW) //2

            if canShip(m):
                shipWeight = m
                maxW = m-1
            else:
                minW = m+1
            
        return shipWeight


