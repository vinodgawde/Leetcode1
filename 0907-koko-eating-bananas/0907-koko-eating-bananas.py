class Solution:
    def totalhr(self, piles, hourly):
        tHr=0
        for i in range(len(piles)):
            tHr += math.ceil(piles[i]/hourly)
        return tHr

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while(low <= high):
            mid = low + (high - low) // 2
            reqtime = self.totalhr(piles, mid)
            if reqtime <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
