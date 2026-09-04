class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_s={}
        char_t={}
        for ch in s:
            char_s[ch]=char_s.get(ch,0)+1
        for ch in t:
            char_t[ch]=char_t.get(ch,0)+1
        return char_s == char_t