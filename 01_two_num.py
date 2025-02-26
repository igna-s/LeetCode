class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Dictionario sujerido
        for i, num in enumerate(nums):
            busqueda = target - num
            if busqueda in num_map:
                return [num_map[busqueda], i]  # Devuelve los indices pedidos
            num_map[num] = i  #Guarda el indice
        return []