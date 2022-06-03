import socket
import json
import pickle

class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = socket.gethostname()
        self.port = 8080
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Aqui deberas intentar conectar al servidor.
            self.socket_cliente.connect((self.host, self.port))

            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje
        response_bytes_length = self.socket_cliente.recv(4)
        response_length = int.from_bytes(
            response_bytes_length, byteorder='big')
        response = bytearray()

        # Recibimos datos hasta que alcancemos la totalidad de los datos
        # indicados en los primeros 4 bytes recibidos.
        while len(response) < response_length:
            read_length = min(4096, response_length - len(response))
            response.extend(self.socket_cliente.recv(read_length))
        bytes_recibidos = self.socket_cliente.recv(100) # Rayos, esto es demasiado poco

        # Debe haber un string para imprimirse
        mensaje, continuar = response.decode()
        # Debe haber un boolean para saber si continuar funcionando

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar

        return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje
        msg_bytes = accion.encode('utf-8')
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        self.socket_cliente.sendall(msg_length + msg_bytes)

        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
