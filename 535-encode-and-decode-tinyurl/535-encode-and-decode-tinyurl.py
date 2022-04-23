class Codec:
    def __init__(self):
        self.longurl={}
        self.shorturl={}
        self.count=0
    def encode(self, longurl: str) -> str:
        if longurl in self.longurl:
            return self.longurl[longurl]
        else:
            self.longurl[longurl]=self.count
            self.shorturl[str(self.count)]=longurl
            self.count+=1
            return str(self.count-1)
    def decode(self, shortUrl: str) -> str:
        return self.shorturl[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))