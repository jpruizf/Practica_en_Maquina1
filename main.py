from claseGestorClientes import GestorClientes
from claseGestorReparacion import GestorReparaciones
import csv
def menu():
    gestor_clientes = GestorClientes()
    gestor_reparaciones = GestorReparaciones()
    print("**********|MENU DE OPCIONES|***********")
    print(" 1 >> VER LISTADO DE CLIENTES Y REPARACIONES")
    print(" 2 >> VER DATOS DE UN CLIENTE Y TODAS LAS REPARACIONES HECHAS EN EL VEHICULO INGRESANDO EL DNI DEL CLIENTE")
    print(" 3 >> VER ESTADO DE REPARACION DEL VEHICULO  Y DATOS DEL TITULAR INGRESANDO LA PATENTE DEL VEHICULO DEL CLIENTE")
    print(" 4 >> VER LISTADO DE CLIENTES CON ESTADO DE REPARACION PENDIENTE")
    print(" 5 >> VER EL O LOS CLIENTES QUE SE LES REALIZO MAS DE UNA REPARACION A SU VEHICULO")
    print(" 6 >> FINALIZAR OPERACION")
    opcion = input(" SELECCIONE UNA DE LAS OPCIONES DADAS >> ")
    while opcion != '0':
        if opcion == '1':
            with open('clientes.csv','r',encoding='utf-8') as archivo:
                lector = csv.reader(archivo,delimiter=';')
                for fila in lector:
                    dni = str(fila[0].split()[0])
                    apellido = str(fila[1].split()[0])
                    nombre = str(fila[2].split()[0])
                    telefono = str(fila[3].split()[0])
                    patente = str(fila[4].split()[0])
                    vehiculo = str(fila[5].split()[0])
                    estado = (fila[6].split()[0])
                    gestor_clientes.cargar_listado_clientes(dni,apellido,nombre,telefono,patente,vehiculo,estado)
                    gestor_clientes.mostrar_listado_clientes()
            patente = 0
            estado = None
            fila = 0
            with open('reparaciones.csv','r',encoding='utf-8') as archivo:
                lector = csv.reader(archivo,delimiter=';')
                for fila in lector:
                    patente = str(fila[0].split()[0])
                    reparacion = str(fila[1].split()[0])
                    precio_repuesto = (fila[2].split()[0])
                    precio_manodeobra = (fila[3].split()[0])
                    estado = (fila[4].split()[0])
                    gestor_reparaciones.cargar_listado_reparaciones(patente,reparacion,precio_repuesto,precio_manodeobra,estado)
                    gestor_reparaciones.mostrar_listado_reparaciones()
        elif opcion == '2':
            auxpatente = gestor_clientes.encontrar_cliente()
            gestor_reparaciones.recibir_patente(auxpatente)
            gestor_reparaciones.sumar_importe()
        elif opcion == '3':
            gestor_clientes.buscar_Vehiculo()
            gestor_reparaciones.pago()
        elif opcion == '4':
            gestor_reparaciones.lista_reparaciones_pendientes()
        elif opcion == '5':
            patente00 = gestor_reparaciones.vehiculos_con_mas_De_una_reparacion()
            print(patente00)
            gestor_clientes.cliente_con_mas_rapraciones(patente00)
        elif opcion == '6':
            return 0
        print("**********|MENU DE OPCIONES|***********")
        print(" 1 >> VER LISTADO DE CLIENTES Y REPARACIONES")
        print(" 2 >> VER DATOS DE UN CLIENTE Y TODAS LAS REPARACIONES HECHAS EN EL VEHICULO INGRESANDO EL DNI DEL CLIENTE")
        print(" 3 >> VER ESTADO DE REPARACION DEL VEHICULO  Y DATOS DEL TITULAR INGRESANDO LA PATENTE DEL VEHICULO DEL CLIENTE")
        print(" 4 >> VER LISTADO DE CLIENTES CON ESTADO DE REPARACION PENDIENTE")
        print(" 5 >> VER EL O LOS CLIENTES QUE SE LES REALIZO MAS DE UNA REPARACION A SU VEHICULO")
        print(" 6 >> FINALIZAR OPERACION")
        opcion = input(" SELECCIONE UNA DE LAS OPCIONES DADAS >> ")
#Algoritmo principal
if __name__ == '__main__':
    menu()