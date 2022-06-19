class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        right,left=len(products)-1,0
        
        for i in range(len(searchWord)):
            while left<len(products) and (len(products[left])<=i or products[left][i]!=searchWord[i]):
                  left+=1
            while right>-1 and (len(products[right])<=i or products[right][i]!=searchWord[i]):
                  right-=1
            temp=min(left+3,right+1)
            res.append(products[left:temp])
        return res
            
            