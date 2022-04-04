class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current=list(map(int,current.split(":")))
        correct=list(map(int,correct.split(":")))
        count=0
        minutes=60*(0-current[0]+correct[0])-current[1]+correct[1]
        for i in [60,15,5,1]:
            count+=minutes//i
            minutes%=i
        return count