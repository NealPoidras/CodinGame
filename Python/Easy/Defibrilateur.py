import sys
import math
#Made by Neal Poidras - 18/11/2020
class Defib:
    num = 0
    name=""
    adress=""
    cellphoneNumber=""
    lon = 0
    lat = 0
    def __init__(self,num=0,name="",adress="",cellphoneNumber="",lon=0,lat=0):
        self.num=num
        self.name=name
        self.adress=adress
        self.cellphoneNumber=cellphoneNumber
        self.lon=lon
        self.lat =lat
    def CalculDist(self,lon,lat):
        x = (self.lon - lon)*math.cos((lat+self.lat)/2)
        y = (self.lat-lat)
        return math.sqrt(x*x+y*y)*6371
    def getName(self):
        return str(self.name)
    
    #Verify the data if you need to
    def display(self):
        return str("num : "+str(self.num)+"name : "+str(self.name)+" adress: "+str(self.adress)+"cellPhoneNumber: "+str(self.cellphoneNumber)+"lon: "+str(self.lon)+"lat: "+str(self.lat))
def transformTab(tab = []):
    defibs = []
    if(len(tab)==0):
        return None
    for t in tab:
        t = t.split(";")
        defib = Defib(int(t[0]),t[1],t[2],t[3],float(t[4].replace(",",".")),float(t[5].replace(",",".")))
        defibs.append(defib)
        defib = None
    return defibs
        

lon = float(input().replace(",","."))
lat = float(input().replace(",","."))

tab = [input() for i in range(int(input()))]

tab = transformTab(tab)
min = sys.maxsize
name = ""

for t in tab:
    #If you wanna check the data
    """
    print(t.display(),file=sys.stderr,flush=True)
    print("distance : ",t.CalculDist(lon,lat),file=sys.stderr,flush=True)"""
    toverify = t.CalculDist(lon,lat)
    if(min>toverify):
        min = toverify
        name = t.getName()
        
print(name)



