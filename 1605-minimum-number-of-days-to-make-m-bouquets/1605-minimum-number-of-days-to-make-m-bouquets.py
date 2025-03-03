class Solution:
    def possible(self, bloomDay, day, m, k):
        count = 0
        nofB = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                count += 1
            else:
                nofB += count//k
                count = 0
        nofB += count//k
        if nofB >= m:
            return True
        return False   


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while(low <= high):
            mid = low + (high - low) // 2
            Bou = self.possible(bloomDay, mid, m, k)
            if Bou == True:
                high = mid - 1
            else:
                low = mid + 1
        return low
        