class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)  # Unimos y ordenamos las listas
        n = len(nums)  # Cantidad total de elementos
        
        if n % 2 == 1:  
            return nums[n // 2]  # Si es impar, devolvemos el del medio
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2.0  # Si es par, promedio de los dos del medio
