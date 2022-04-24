class UndergroundSystem:

    def __init__(self):
        self.d={}
        self.freq=defaultdict(int)
        self.station=defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        curr=self.d.pop(id)
        self.station[(curr[0],stationName)]+=t-curr[1]
        self.freq[(curr[0],stationName)]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station[(startStation,endStation)]/self.freq[(startStation,endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)