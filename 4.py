class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        clist = sorted(nums1+nums2)
        if len(clist)%2==0:
            return float((float(clist[len(clist)/2-1]) + float(clist[len(clist)/2]))/2)
        else:
            return clist[len(clist)]//2
