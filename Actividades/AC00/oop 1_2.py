'''
Probando propiedades de los objetos
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


# Ejemplo de funcionamiento

m1 = Email('kp1@othermail.com')
print(m1.email)
m1.email = "kp2@com"
print(m1.email)

    
