

class Reparacion:
    __patente: str
    __reparacion: str
    __precioRepuesto: int
    __precioManoDeObra: int
    __estado: str
    def __init__(self,patente,reparacion,precioRepuesto,precio_ManoDeObra,estado):
        self.__patente = patente
        self.__reparacion = reparacion
        self.__precioRepuesto = precioRepuesto
        self.__precioManoDeObra = precio_ManoDeObra
        self.__estado = estado
    def get_Patente(self):
        return self.__patente
    def get_reparacion(self):
        return self.__reparacion
    def get_precioRepuesto(self):
        return self.__precioRepuesto
    def get_precioManoDeObra(self):
        return self.__precioManoDeObra
    def get_estado(self):
        return self.__estado
        
