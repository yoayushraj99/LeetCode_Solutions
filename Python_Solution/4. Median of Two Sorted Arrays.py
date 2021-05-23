class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) == 0 and len(nums2) == 1: return nums2[0]
        if len(nums2) == 0 and len(nums1) == 1: return nums1[0]

        i, j = 0, 0

        merged_array = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1

        merged_array = merged_array + nums1[i:] + nums2[j:]

        middle = int((len(merged_array) - 1) / 2)
        n1 = merged_array[middle]

        if len(merged_array) % 2 != 0:
            return n1

        n2 = merged_array[middle + 1]

        median = (n1 + n2) / 2

        return median
