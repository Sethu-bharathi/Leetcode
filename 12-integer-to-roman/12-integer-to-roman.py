class Solution:
    def intToRoman(self, num: int) -> str:
        
        dic = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'}
        
        
        numbers = list(dic.keys())[::-1]
        
        ans = []
        for nd in numbers:
            div1, mod1 = divmod(num, nd)
            if div1 > 0:
                ans.append(div1*dic[nd])
            num = mod1
        
        return ''.join(ans)