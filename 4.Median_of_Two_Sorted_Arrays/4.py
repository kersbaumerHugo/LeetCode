class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine_arr = nums1+nums2
        combine_arr.sort()
        if len(combine_arr)%2==0:
            median = (combine_arr[int(len(combine_arr)/2)]+combine_arr[int(len(combine_arr)/2)-1])/2
        else:
            median = combine_arr[int(floor(len(combine_arr)/2))]
        return median
