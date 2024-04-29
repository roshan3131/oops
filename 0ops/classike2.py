

class Bike:
  def _init_(self,name,cc):
    self.bike_name=name
    self.bike_cc=cc

  def _Type(self):
     if self.bike_cc<200:
        print(f"{self.bike_name} is normal bike")
     else:
        print(f"{self.bike_name} is superbike")

Duke=Bike("RC390",390)
RE=Bike("classic350",350)
Hero=Bike("Splender",110)

b=input("enter the bike:")
if(b=="Duke"):
  Duke._Type()
elif(b=="RE"):
  RE. _Type()
else:
  Hero._Type()