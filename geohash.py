import pygeohash as p 
class geohash:
    def __init__(self,lat,long):
        self.lat=float(lat)
        self.long=float(long)
        
    def hash(self):
        h=p.encode(self.lat,self.long)
        return h


