import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        k="".join([char for char in t if char not in                        string.punctuation]).replace(" ","")
        t=k[::-1]
        if k==t:
            return True
        
        return False
        