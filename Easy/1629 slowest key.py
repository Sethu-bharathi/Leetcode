class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        if len(releaseTimes)==1:
            return keysPressed
        maxtime=releaseTimes[0]
        maxstr=keysPressed[0]
        for i in range(1,len(releaseTimes)):
            curtime=releaseTimes[i]-releaseTimes[i-1]
            if curtime>maxtime:
                maxtime=curtime
                maxstr=keysPressed[i]
            elif curtime==maxtime:
                if maxstr<keysPressed[i]:
                    maxstr=keysPressed[i]
        return maxstr
Time=list(map(int,input("enter the keyTime").split()))
keys=input("enter the string")
key1=Solution()
print(key1.slowestKey(Time,keys))