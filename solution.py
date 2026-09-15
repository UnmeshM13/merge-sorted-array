class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mydict = dict()
        for i in nums1[:m]:
            if i not in mydict:
                mydict[i]=1
            else:
                mydict[i]+=1

        for i in nums2[:n]:
            if i not in mydict:
                mydict[i]=1
            else:
                mydict[i]+=1
        keys = sorted(mydict.keys())      
        k = 0

        for key in keys:
            for _ in range(mydict[key]):
                nums1[k] = key
                k += 1