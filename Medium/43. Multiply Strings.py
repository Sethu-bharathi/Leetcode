class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n2=0
        n1=0
        ore=ord
        for i in num2:
            n2*=10
            n2+=ore(i)-48
        for i in num1:
            n1*=10
            n1+=ore(i)-48
        n1*=n2
        if n1==0:
            return "0"
        num1=""
        while n1:
            num1=chr((n1%10)+48)+num1
            n1//=10
        return num1
        