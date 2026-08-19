class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1, countWin = defaultdict(int), defaultdict(int)

        for char in s1:
            count1[char] += 1
        
        l = 0
        windowSize = len(s1) - 1
        for r in range(len(s2)):

            c = s2[r]
            countWin[c] +=1
            #print(countWin, r-l, windowSize)
            
            
            if r-l > windowSize:
                countWin[s2[l]] -=1
                if countWin[s2[l]] == 0:
                    del countWin[s2[l]]
                l+=1
            
            if r-l == windowSize and countWin == count1:
                return True
            
            
            
        return False

