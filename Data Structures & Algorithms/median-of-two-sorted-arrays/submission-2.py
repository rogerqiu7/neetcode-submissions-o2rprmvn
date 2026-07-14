class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        mid = length // 2

        if length % 2 == 0:
            return (merged[mid] + merged[mid - 1]) / 2
        else:
            return merged[mid]