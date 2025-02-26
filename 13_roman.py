class Solution(object):
    def romanToInt(self, s):
        # Valores romanos
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000
        }

        total = 0
        # Recorro
        for i in range(len(s)):
            # Si el caracter que sigue es menor sumo
            if i == len(s) - 1 or values[s[i]] >= values[s[i + 1]]:
                total += values[s[i]]
            else:
                # Sino resto
                total -= values[s[i]]
        return total