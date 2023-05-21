

class Cliente:
    __dni: str
    __apellido: str
    __nombre: str
    __telefono: str
    __patente: str
    __vehiculo: str
    __estado: str
    def __init__(self,dni,apellido,nombre,telefono,patente,vehiculo,estado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__patente = patente
        self.__vehiculo = vehiculo
        self.__estado = estado
    def get_Dni(self):
        return self.__dni
    def getApellido_Nombre(self):
        return (self.__apellido,self.__nombre)
    def get_Telefono(self):
        return self.__telefono
    def get_Patente(self):
        return self.__patente
    def get_Vehiculo(self):
        return self.__vehiculo
    def get_Estado(self):
        return self.__estado
    def buscar(self,dni):
        encontrado = False
        valor = None
        while not encontrado:
            if self.get_Dni() == dni:
                encontrado = True
                valor = dni
            else:
                valor = -1
        if encontrado and valor != -1:
            return valor
        else:
            print("¡Cliente no encontrado!")
    def vehiculo(self,patente):
        encontrado = False
        valor = None
        while not encontrado and valor == -1:
            if self.get_Patente() == patente:
                encontrado = True
                valor = patente
            else:
                valor = -1
                encontrado =  True
        if encontrado and valor != -1:
            return self.get_Patente()