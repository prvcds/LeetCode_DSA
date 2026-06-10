class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total = 1
        for x in nums:
            total *= x

        if total != target * target:
            return False

        n = len(nums)

        for mask in range(1, (1 << n) - 1):
            p = 1

            for i in range(n):
                if mask & (1 << i):
                    p *= nums[i]
                    if p > target:
                        break

            if p == target:
                return True

        return False