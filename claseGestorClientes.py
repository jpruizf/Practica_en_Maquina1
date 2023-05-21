from clasecliente import Cliente

class GestorClientes:
    __cliente: object
    __lista_clientes: list
    def __init__(self):
        self.__lista_clientes = []
        
    def cargar_listado_clientes(self,dni,apellido,nombre,telefono,patente,vehiculo,estado):
        self.__cliente = Cliente(dni,apellido,nombre,telefono,patente,vehiculo,estado)
        self.__lista_clientes.append(self.__cliente)
        return self.__lista_clientes
    def mostrar_listado_clientes(self):
        i = 0
        for i in  range(i,len(self.__lista_clientes)): 
            print(f"{self.__cliente.get_Dni()} | {self.__cliente.getApellido_Nombre()} | {self.__cliente.get_Telefono()} | {self.__cliente.get_Patente()} | {self.__cliente.get_Vehiculo()} | {self.__cliente.get_Estado()}")
    def encontrar_cliente(self):
        bandera = True
        auxdni = str(input("Ingrese el dni de un cliente >>"))
        valor = self.__cliente.buscar(auxdni)
        i = 0
        while bandera and i < len(self.__lista_clientes):
            if valor == self.__lista_clientes[i].get_Dni():
                bandera = False
                print(f" Cliente encontrado! >> {self.__lista_clientes[i].get_Dni()} | {self.__lista_clientes[i].getApellido_Nombre()} | {self.__lista_clientes[i].get_Patente()} | {self.__lista_clientes[i].get_Vehiculo()}")
            else:
                i += 1
        return self.__cliente.get_Patente()
    def buscar_Vehiculo(self):
        i = 0
        bandera = True
        auxipatente = str(input("Ingrese la patente del vehiculo >> "))
        str(self.__cliente.vehiculo(auxipatente))
        while bandera and i < len(self.__lista_clientes):
            if self.__lista_clientes[i].get_Estado() == "T":
                bandera = False
                print(f"Vehiculo encontrado! >> Titular > > {self.__lista_clientes[i].getApellido_Nombre()} | Telefono > > {self.__lista_clientes[i].get_Telefono()} | Vehiculo > > {self.__lista_clientes[i].get_Vehiculo()} | Patente > > {self.__lista_clientes[i].get_Patente()}")
            else:
                i += 1
    def cliente_con_mas_rapraciones(self,patente00):
        x = self.__eq__(patente00)
        if x:
            print(f"{self.__cliente.get_Dni()} | {self.__cliente.getApellido_Nombre()} | {self.__cliente.get_Telefono()} | {self.__cliente.get_Patente()} | {self.__cliente.get_Vehiculo()}")
        else:
            print("Error inesperado :/")
    def __eq__(self, otro):
        i = 0
        bandera = False
        while i < len(self.__lista_clientes) and not bandera:
            if otro == self.__lista_clientes[i].get_Patente():
                bandera = True
            i += 1
        return bandera
        