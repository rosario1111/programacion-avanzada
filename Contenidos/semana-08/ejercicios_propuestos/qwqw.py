from collections import namedtuple, defaultdict

# Modelamos los clientes
Cliente = namedtuple('Cliente', ['ticket', 'nombre', 'apellido'])


class ErrorTratanDeRobar(Exception):
    conteo = defaultdict(int)

    def __init__(self, cliente):
        self.nombre = cliente.nombre
        self.ticket = cliente.ticket
        self.conteo[self.ticket] += 1

    @property
    def cantidad_repeticiones(self):
        return self.conteo[self.ticket]


# Modelamos la tienda con una estructura simple para almacenar sus clientes
class Tienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = dict()

    # Método encargado de entregar un completo, en caso de encontrar duplicado, lanza error
    def recibir(self, cliente):
        if cliente.ticket in self.clientes:
            raise ErrorTratanDeRobar(cliente)
        else:
            self.clientes[cliente.ticket] = cliente
            print(f'✅ Cliente {cliente.nombre} de ticket {cliente.ticket} ha recibido su completo exitosamente.\n')


if __name__ == "__main__":

    clientes_que_no_han_comido = [
        Cliente('1', 'Daniela', 'Poblete'),
        Cliente('2', 'Tomás', 'González'),
        Cliente('3', 'Enzo', 'Tamburirni'),
        Cliente('4', 'Daniela', 'Concha'),
        Cliente('2', 'Dante', 'Pinto'),
        Cliente('5', 'Juan', 'Aguillon'),
        Cliente('1', 'Caua', 'Paz'),
        Cliente('6', 'Máx', 'Narea'),
        Cliente('1', 'Javiera', 'Ochoa')
    ]

    DCCompletos = Tienda('DDCompletos')

    for cliente in clientes_que_no_han_comido:
        try:
            DCCompletos.recibir(cliente)
        except ErrorTratanDeRobar as error:
            print(f'❌ Cliente {error.nombre} tratando de robar un completo con el ticket {error.ticket} encontrado')
            print(f'Ya van {error.cantidad_repeticiones} repetidos para el ticket {error.ticket}')
            print()
