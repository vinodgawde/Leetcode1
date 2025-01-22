class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_from_right = -1
        for i in range(len(arr)-1,-1,-1):
            current_pos = arr[i]
            arr[i] = max_from_right
            if max_from_right < current_pos:
                max_from_right = current_pos
        return arr


        