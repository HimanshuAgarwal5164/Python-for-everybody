class car:
    def __init__(self,a=50):
        self._speed=a
        return
    def getspeed(self):
        return self._speed
    def setspeed(self,s):
        if s<0 or s>200:
            print("speed should be between 0 and 200")
        else:
            self._speed=s
        return
    speed=property(getspeed,setspeed)




c=car()
x=c.speed
print(x)
s=int(input("Enter speed"))
c.speed=s
x=c.speed
print(x)
