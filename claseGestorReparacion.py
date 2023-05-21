from clasereparacion import Reparacion

class GestorReparaciones:
    __lista_reparaciones: list
    __reparacion: object
    def __init__(self):
        self.__lista_reparaciones = []
    def cargar_listado_reparaciones(self,patente,reparacion,precioReparacion,precioManoDeObra,estado):
        self.__reparacion = Reparacion(patente,reparacion,precioReparacion,precioManoDeObra,estado)
        self.__lista_reparaciones.append(self.__reparacion)
    def mostrar_listado_reparaciones(self):
        i = 0
        for i in range(i,len(self.__lista_reparaciones)):
            print(f"{self.__reparacion.get_Patente()} | {self.__reparacion.get_reparacion()} | {self.__reparacion.get_precioRepuesto()} | {self.__reparacion.get_precioManoDeObra()} | {self.__reparacion.get_estado()}")
    def recibir_patente(self,auxpatente):
        i = 0
        bandera = True
        while i < len(self.__lista_reparaciones) and bandera:
            if self.__lista_reparaciones[i].get_Patente() != auxpatente:
                i += 1
            else:
                bandera = False
                print(f"{self.__lista_reparaciones[i].get_reparacion()} | {self.__lista_reparaciones[i].get_precioRepuesto()} | {self.__lista_reparaciones[i].get_precioManoDeObra()}")
    def sumar_importe(self):
        subtotal_importe = 0
        total_importe = 0
        i = 0
        for i in range(i,len(self.__lista_reparaciones)):
            subtotal_importe = int(self.__reparacion.get_precioRepuesto()) + int(self.__reparacion.get_precioManoDeObra())
            total_importe += subtotal_importe
        print(f"Subtotal a pagar: {subtotal_importe} | TOTAL A PAGAR: {total_importe}")
    def pago(self):
        i = 0
        total_importe = 0
        for i in range(i,len(self.__lista_reparaciones)):
            total_importe += int(self.__reparacion.get_precioRepuesto()) + int(self.__reparacion.get_precioManoDeObra())
        print(f"TOTAL A PAGAR : {total_importe}")    
    def lista_reparaciones_pendientes(self):
        i = 0
        for i in range(i,len(self.__lista_reparaciones)):
            if self.__lista_reparaciones[i].get_estado() == 'P':
                print(f"{self.__reparacion.get_Patente()} | {self.__reparacion.get_reparacion()} | {self.__reparacion.get_precioRepuesto()} | {self.__reparacion.get_precioManoDeObra()} | {self.__reparacion.get_estado()}")
    def vehiculos_con_mas_De_una_reparacion(self):
        i = 0
        encontrado = False
        while i < len(self.__lista_reparaciones) and  not encontrado:
            if self.__lista_reparaciones[i].get_estado() == 'T':
                encontrado = True
            else:
                i += 1
        if encontrado:
            return self.__lista_reparaciones[i].get_Patente()
        else:
            return None