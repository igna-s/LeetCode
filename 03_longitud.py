class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maximo = 0
        start = 0
        mi_set = set()

        for act in range(len(s)):
            while s[act] in mi_set:
                mi_set.remove(s[start])
                start += 1
            mi_set.add(s[act])
            maximo = max(maximo, act - start + 1)
        
        return maximo
