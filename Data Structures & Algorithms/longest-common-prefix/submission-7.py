class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        shortest_length = len(strs[0])
        while shortest_length>0:
            strs = [s[:shortest_length] for s in strs]
            if len(set(strs)) == 1:
                return strs[0]
            else:
                shortest_length-=1
        return ""
        