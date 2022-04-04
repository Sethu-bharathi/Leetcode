class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins={}
        loses={}
        for i in matches:
            if i[0] in wins:
                wins[i[0]]+=1
            else:
                wins[i[0]]=1
            if i[1] in loses:
                loses[i[1]]+=1
            else:
                loses[i[1]]=1
        winner=[]
        losers=[]
        for i in wins:
            if i not in loses:
                winner.append(i)
        for i in loses:
            if loses[i]==1:
                losers.append(i)
        return [sorted(winner),sorted(losers)]