class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index=0
        arr=[0 for i in range(1001)]
        for i in arr1:
            arr[i]+=1
        for i in arr2:
            while arr[i]>0:
                arr1[index]=i
                arr[i]-=1
                index+=1
        for i in range(len(arr)):
            while arr[i]>0:
                arr1[index]=i
                arr[i]-=1
                index+=1
        return arr1