class Solution:
    def generateRow(self, row: int) -> List[int]:
        ans = 1
        ansRow = [1]  
        for col in range(1,row):
            ans = ans * (row - col) // col
            ansRow.append(ans)
        return ansRow

    def generate(self, numRows: int) -> List[List[int]]:
        main = []
        for i in range(numRows):
            main.append(self.generateRow(i + 1))
        return main