class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {i:0 for i in s}
        dict_t = {i:0 for i in t}
        for i in s:
            dict_s[i] += 1
        for i in t:
            dict_t[i] += 1
        return dict_s == dict_t