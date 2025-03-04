class Solution:
    def capcity(self, weights, cap):
        days = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i] > cap:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low <= high):
            mid = low + (high - low) // 2
            dayReq = self.capcity(weights,mid)
            if dayReq <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
                