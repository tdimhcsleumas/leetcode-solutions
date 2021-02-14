class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A = []
        
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                A.append(nums1.pop(0))
            else:
                A.append(nums2.pop(0))
        
        while len(nums1) > 0:
            A.append(nums1.pop(0))
            
        while len(nums2) > 0:
            A.append(nums2.pop(0))
            
        if len(A) % 2 == 0:
            i = len(A)//2-1;
            j = len(A)//2;
            return (A[i]+A[j])/2.0;
        return A[len(A)//2]
        
