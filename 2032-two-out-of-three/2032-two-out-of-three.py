class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        set1= set(nums1)
        set2=set(nums2)
        set3=set(nums3)
        result=set1.intersection(set2)
  
        result2 = set1.intersection(set3)

        result3= set2.intersection(set3)
  
        final = result.union(result2, result3)
        return list(final)
        