class circle():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.r=self.radius()
    def radius(self):
        return abs(self.x*self.y)
    def position(self,other):
        mesafe=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        if abs((other.r-self.r))<abs(mesafe)<abs((other.r+self.r)):
            return ("bu çemberler kesişiyor")
        elif mesafe==abs((other.r-self.r)) or mesafe==abs((other.r+self.r)):
            return ("bu çemberler tegettir")
        elif mesafe > (other.r+self.r) or mesafe<abs((other.r-self.r)):
             return "bu çemberler kesişmiyor"
       
    def getarea(self):
        area=3*(self.r**2)
        return area
    def getperimeter(self):
        cevre=3*2*self.r
        return cevre
x=int(input())
y=int(input())
circle1=circle(x,y)
x=int(input())
y=int(input())
circle2=circle(x,y)
print(circle1.position(circle2))
print("circle"+"M",(circle1.x,circle1.y))
print("radius=",circle1.radius())
print("area=",circle1.getarea())
print("perimeter=",circle1.getperimeter())
print("circle"+"M",(circle2.x,circle2.y))
print("radius=",circle2.radius())
print("area=",circle2.getarea())
print("perimeter=",circle2.getperimeter())

