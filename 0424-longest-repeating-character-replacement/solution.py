class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostCommon = ["*", 0]
        chars = defaultdict(int)
        maxWindow, numDiff, l = -1,0,0
    
        for r in range(len(s)):

            chars[s[r]] += 1
            if chars[s[r]] > mostCommon[1]:
                mostCommon[0], mostCommon[1] = s[r], chars[s[r]]
                
            numDiff = sum(chars.values()) - mostCommon[1]
            if numDiff <= k: #Have a valid replacement available
                maxWindow = max(maxWindow, r-l)
            else:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            
        return maxWindow+1


