class Solution:
    def minimumLines(self, stockprices: List[List[int]]) -> int:
        def slope(x1,x2,y1,y2):
            return (y2-y1),(x2-x1)
        
        stockprices.sort()
        n=len(stockprices)
        if n==1:
            return 0  
        count=1
        for i in range(1,n-1):
            x1,y1=stockprices[i-1]
            x2,y2=stockprices[i]
            x3,y3=stockprices[i+1]
            
            if (y1-y2)*(x2-x3)!=(y2-y3)*(x1-x2):
                count+=1
        return count
            