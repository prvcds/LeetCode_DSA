from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = defaultdict(int)
        four_sums = 0

        for n1 in nums1:
            for n2 in nums2:
                hash_map[n1 + n2] += 1

        for n3 in nums3:
            for n4 in nums4:
                four_sums += hash_map[-(n3 + n4)]
        
        return four_sums