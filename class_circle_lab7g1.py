class Circle:
    #class attribute
    pi=3.14
    def __init__(self,x,y): #noktanın koordinat bilgilerini tutan method
        self.x=x            #c1(x1,y1) c2(x2,y2)
        self.y=y
        self.r=self.radius()

    #methods
    def radius(self): #yarıçapı bu şekilde aldığımızı varsayalım
        return self.x*self.y

    def position(self,other): #iki çemberin durumunu veren  method
        distance=(((self.x-other.x)**2+(self.y-other.y)**2)*0.5)
        if abs(self.r-other.r)<distance<(self.r+other.r):
            return "Bu cemberler kesisiyor"
        elif abs(self.r-other.r)==distance or (self.r+other.r)==distance:
            return " Bu cemberler teget."
        elif abs(self.r-other.r)>distance or distance> (self.r+other.r):
            return " Bu cemberler kesismiyor."
        
    def getArea(self): #alan hesaplayan method
        pi=3
        self.alan=round(self.pi*(self.r)**2,2)
        return self.alan
    
    def getPerimeter(self): #çevre hesaplayan method
        pi=3
        self.uzunluk=2*self.pi*self.r
        return self.uzunluk
    
    def __str__(self): #classın string çıktısını veren method 
        return f'circle M{self.x,self.y}/n radius={c1.x,c1.y}/n area={c1.radius()}/n '
x=int(input())
y=int(input())
c1=Circle(x,y)
x=int(input())
y=int(input())
c2=Circle(x,y)
print(c1.position(c2))
print(Circle.position(c1,c2))


# Output:
# Bu cemberler kesisiyor.
# Circle = M(1,2)
# Radius = 2
# Area = 12
# Perimeter = 12
# Circle = M(2,1)
# Radius = 2
# Area = 12
# Perimeter = 12