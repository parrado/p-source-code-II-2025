from math import pi,sqrt

# Base/parent class is abstract
class Shape:
    def __init__(self,centerX,centerY):
        self._centerX=centerX
        self._centerY=centerY
    
    # area must be implementd by child classes (Abstract method)
    # (polymorphism)
    def area(self):
        pass
    
    def showCoordinates(self):
        print(f'My coordinates are ({self._centerX},{self._centerY})')

# Circle inherits from Shape
class Circle(Shape):
    
    def __init__(self,centerX,centerY,radius):
        super().__init__(centerX,centerY) # Call constructor of Shape
        self.radius=radius
        
    # Implement area 
    def area(self):
        return pi*self.radius**2

# Triangle inherits from Shape
class Triangle(Shape):
    def __init__(self,centerX,centerY,base,height):
        super().__init__(centerX,centerY)
        self.height=height
        self.base=base
        

    def area(self):
        return self.base*self.height/2
    
    def coord(self):
        print(self._centerX,self._centerY)

class RectTriangle(Triangle):
    def __init__(self,centerx,centery,base,height):
        super().__init__(centerx,centery,base,height)
        self.hyp=sqrt(self.base*self.base+self.height*self.height)
    
    def showHyp(self):
        print(f'My hypotenuse is {self.hyp}')
    
    def showCoordinates(self):
        print(f'I\'m a rect triangle and')
        super().showCoordinates()
    
# Object Circle of radius 1    
myCircle0=Circle(-2.0,2.0,1.0)

# Object Triangle of base 5 and height 3
myTriangle0=Triangle(0.1,0.1,5.0,3.0)

aCircle=myCircle0.area()
aTriangle=myTriangle0.area()

print(f'El área del círculo es: {aCircle}')
print(f'El área del triángulo es: {aTriangle}')
myCircle0.showCoordinates()
myTriangle0.showCoordinates()
myTriangle0.coord()

rectTriangle0=RectTriangle(0,0,2,2)
rectTriangle0.showHyp()
rectTriangle0.showCoordinates()



