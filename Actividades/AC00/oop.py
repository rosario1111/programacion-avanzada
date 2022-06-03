### PROGRAMACIÓN ORIENTADA A OBJETOS ###


class Apartment:
    def __init__(self,_id,mts2,value):
        self._id = _id
        self.mts2 = mts2
        self.value = value
        self.sold = False

    def sell(self):
        if not self.sold:
            '''
            'not' es un operador que regresa True si el statement no es verdadero
             si es que es falso, vuelvelo verdadero.
             osea, al llamar a nombre_objeto.sell, cambio el atributo a que se vendio (verdadero)
             '''
            self.sold = True

        else:
            print("Apartment {} was sold"
                  .format(self._id))

# from create_apartment import Apartment

d1 = Apartment(_id=1, mts2=100, value=5000) #creo el primer objeto

print("sold?", d1.sold)
d1.sell() #le decimos al objeto que se vendió
print("sold?", d1.sold)
d1.sell()
 
''' __init__ método (función de un objeto)
que inicia la instancia dejando los atributos con los valores
iniciales, pasados como argumentos.
self, todo lo que venga en init tiene que ir con self para poder
llamarse a si mismo.
'''

help(Apartment)
