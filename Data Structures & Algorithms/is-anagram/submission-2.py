class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = {}
        t_chars = {}

        for char in s:
            if char in s_chars:
                s_chars[char] += 1
            else:
                s_chars[char] = 1
        
        for char in t:
            if char in t_chars:
                t_chars[char] += 1
            else:
                t_chars[char] = 1
        
        if len(s_chars) != len(t_chars):
            return False
        

        for key, value in s_chars.items():
            if key in t_chars:
                if t_chars[key] == value:
                    continue
                else:
                    return False
            return False
        
        return True

        
        