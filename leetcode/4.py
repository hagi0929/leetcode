class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1[:]+nums2[:]
        l.sort()
        r=0
        if len(l)%2 !=0:
            r=l[len(l)//2]
        else:
            r=sum(l[len(l)//2 - 1 : len(l)//2 + 1]) / 2
        return r