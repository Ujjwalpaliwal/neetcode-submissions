from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of '#'
            while j < len(s) and s[j] != '#':
                j += 1
            
            # Extract the length (not j-i, but the numeric value)
            length = int(s[i:j])
            
            # Extract the string
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            # Move to the next string
            i = end
        
        return decoded