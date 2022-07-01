class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        count=0
        for i in boxTypes:
            if truckSize>=i[0]:
                truckSize-=i[0]
                count+=i[0]*i[1]
            else:
                count+=truckSize*i[1]
                return count
        return count