class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        l, r, hi, lo = 0, -1, -inf, inf  # sorted array -> r - l + 1 == 0
        for i, (x, y) in enumerate(zip(nums, reversed(nums))):
            if x < (hi := max(hi, x)): r = i  # something bigger is to the left -> x is misplaced
            if y > (lo := min(lo, y)): l = len(nums) - 1 - i  # something smaller is to the right -> y is misplaced
        return r - l + 1