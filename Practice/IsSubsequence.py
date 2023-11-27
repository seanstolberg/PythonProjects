class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        is_sub = False

        while s_index < len(s):
            while t_index < len(t):
                if t[t_index] == s[s_index]:
                    if s_index == len(s) - 1:
                        is_sub = True
                    t_index += 1
                    break
                t_index += 1
            s_index += 1
        
        return is_sub





print(Solution.isSubsequence(s = "abc", t = "ahbgdc")) #true
print(Solution.isSubsequence(s = "axc", t = "ahbgdc")) #false