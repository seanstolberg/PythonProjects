class Solution:
    def letterCombinations(digits: str) -> list[str]:
        res = []
        digitsToChar = {"2" : "abc",
                  "3" : "def",
                  "4" : "ghi",
                  "5" : "jkl",
                  "6" : "mno",
                  "7" : "qprs",
                  "8" : "tuv",
                  "9" : "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res
    
print(Solution.letterCombinations(digits = "23"))