# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search: the first bad version is somewhere between low and high
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid       # mid is bad, so the first bad is mid or earlier
            else:
                low = mid + 1    # mid is good, so the first bad is after mid
        return low
        