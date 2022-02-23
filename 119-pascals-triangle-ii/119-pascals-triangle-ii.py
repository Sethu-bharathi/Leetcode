class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<2:
            return [1 for i in range(rowIndex+1)]
        arr=[1]
        for j in range(rowIndex):
            for i in range(len(arr)-1):
                arr[i]+=arr[i+1]
            arr=[1]+arr
        return arr