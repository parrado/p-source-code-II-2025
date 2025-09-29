from math import pi

# Define clase Circulo con 3 atributos
class Circulo:
    # Función constructor, se llama cuando se crea el objeto
    # El constructor define 3 atributos
    def __init__(self,radioi,centroXi,centroYi):
        self.radio=radioi
        self.centroX=centroXi
        self.centroY=centroYi        

    # Se definen dos métodos para la clase Circulo
    def area(self):
        return pi*self.radio**2
    
    def perimetro(self):
        return 2*pi*self.radio
    
class Rectangle:
    pass