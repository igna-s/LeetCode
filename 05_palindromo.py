class Solution(object):
    def longestPalindrome(self, s):

        longest = ""
        if not s:
            return longest

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            # Palíndromo de longitud impar
            odd = expandAroundCenter(i, i)
            # Palíndromo de longitud par
            even = expandAroundCenter(i, i + 1)

            # Actualizamos el palíndromo más largo encontrado
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
