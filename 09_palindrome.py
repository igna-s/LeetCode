class Solution(object):
    def isPalindrome(self, x):
        if (x<0):
             return False
        x = str(x)
        start = 0
        end = len(x)
        for aux in range(len(x) // 2):
            if x[start] != x[end-1]:
                return False
            start = start+1
            end = end -1
        return True

        