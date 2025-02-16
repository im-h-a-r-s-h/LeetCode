class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p=m-1
        q=n-1
        i=0
        for i in range(m+n-1,0,-1):
            if q<0:
                nums1[i]=nums1[p]
                p=p-1
            elif p<0:
                nums1[i]=nums2[q]
                q=q-1
            elif(nums1[p]>=nums2[q]):
                nums1[i]=nums1[p]
                p=p-1
            else:
                nums1[i]=nums2[q]
                q=q-1
            i=i-1
        if i==0:
            if q<0:
                nums1[i]=nums1[p]
            elif p<0:
                nums1[i]=nums2[q]
