class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        feq={}
        for ch in s:
            feq[ch]=feq.get(ch,0)+1
        for ch in t:
            if ch not in feq:
                return False
            feq[ch]-=1
            if feq[ch]<0:
                return False
        return True


    