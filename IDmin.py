n=int(input())
products=list(map(int,input().split()))

count={}
maxi=0
mini=10000
maxid=-1
minid=-1
for i in products:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in count:
    if maxi<count[i]:
        maxi=count[i]
        maxid=i
    if mini>count[i]:
        mini=count[i]
        minid=i
if maxi==mini:
    print(0)
if maxid>minid:
    print(maxi-mini)
else:
    maxi=0
    for i in count:
        if minid<i:
            maxi=max(maxi,count[i])
    if maxi!=0:
        print(maxi-mini)
    else:
        print(0)

