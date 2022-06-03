### Actividad 00 ###

import math 

class Circulo:

    def __init__(self,x ,y, radio): #(x,y) son las coordenadas de origen)
        self.x = x
        self.y = y
        self.radio = radio

    def obtener_area(self):
        area = (self.radio**2)*math.pi
        return str(area)

    def obtener_perimetro(self):
        perimetro = 2*self.radio*math.pi
        return str(perimetro)

    def __str__(self):
        return ("Esta figura es un círculo que tiene un área de {} y un perímetro de {}"
                 .format(self.obtener_area(),self.obtener_perimetro()))
                


class Rectangulo:

    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def obtener_area(self):
        area = self.lado1*self.lado2
        return print(str(area))

    def obtener_perimetro(self):
        perimetro = 2*self.lado1 + 2*self.lado2
        return print(str(perimetro))

    def __str__(self):
        return 
    

circulo1 = Circulo(0,0,3)
circulo1.obtener_area()
print(circulo1)

rectangulo1 = Rectangulo(2,3)
    

        
