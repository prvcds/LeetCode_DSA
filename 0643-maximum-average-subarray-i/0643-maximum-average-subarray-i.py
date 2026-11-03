class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        xx = sum(nums[:k])
        x = round(xx/k,5)

        for i in range(k,len(nums)):
            xx += nums[i] - nums[i-k]
            x = max(round(xx/k,5),x)

        return x  