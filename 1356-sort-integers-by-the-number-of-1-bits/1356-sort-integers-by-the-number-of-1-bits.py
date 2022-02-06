class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key=lambda a:(self.count1(a),a))
    def count1(self,n):
        count=0
        while n:
            count+=1
            n=n&(n-1)
        return count