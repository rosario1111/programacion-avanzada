'''
Probando propiedades de los objetos
'''

'''
property() permite crear una propiedad, reciviendo de argumentos
las funciones, get, set y delete del atributo
prpoerty(<setter_function>,<getter_funtion>,<deleter_function>)
'''

class Email:

    def __init__(self, address):
        self._email = address #atributo privado

    def _set_email(self, value):
        if '@' not in value:
            print("This is not an email address.")
        else:
            self._email = value

    def _get_email(self):
        return self._email

    def _del_email(self):
        print("Erase this email attribute!!")
        del self._email

    # La interfaz provee el atributo público 'email'

    email = property(_get_email, _set_email, _del_email,
                     'This property contains the email.')

'''
La primera diferencia que vemos entre los códigos anteriores
es el uso de __ antes de mi_atributo. Cuando nombramos una variable de esta
manera, es una forma de decirle a Python que queremos
que se “oculte” y que no pueda ser accedida como el resto de atributos.
'''

# Ejemplo de funcionamiento

m1 = Email('kp1@othermail.com')
print(m1.email)
m1.email = "kp2@com" #se puede usar tanto con _ como sin el
print(m1.email)

    
