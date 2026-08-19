class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        countP, countWin, res = defaultdict(int), defaultdict(int), []
        for char in p:
            countP[char] += 1
        
        windowSize = len(p)-1
        l = 0
        for r in range(len(s)):
            c = s[r]
            if r-l < windowSize:
                countWin[c] += 1
                continue
            
            countWin[c] += 1
            
            if countP == countWin:
                res.append(l)
            
            countWin[s[l]] -= 1
            if countWin[s[l]] == 0:
                del countWin[s[l]]
            l += 1
        
        return res

                
            
            
            

                




        
