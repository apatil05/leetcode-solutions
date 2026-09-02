class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        path = []
        res = []

        n = len(digits)

        def backtrack(i): #i represents the current index we are at within our digits array
            #our path is a valid string
            if i >= n:
                res.append("".join(path))
                return

            #our path is not at max depth, so we add a char to path
            letters = keypad[digits[i]]
            for c in letters:
                path.append(c)
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return res


            
            
            
        
