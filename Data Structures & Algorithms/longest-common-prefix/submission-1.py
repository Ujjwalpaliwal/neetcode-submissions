class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        first = strs[0]
        for i in range(len(strs[0])):
            char = first[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return first[:i]
        return first
