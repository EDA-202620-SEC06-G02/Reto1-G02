import sys
import App.logic as logic
from tabulate import tabulate

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    result = logic.load_data(control)
    
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    encontrado = None
    for order in control["chocolate_sale"]["elements"]:
        if order["Order_ID"] == id and encontrado is None:
            encontrado = order
    
    if encontrado is None:
        print("No se encontro")
    else:
        print(tabulate([encontrado], headers="keys", tablefmt="fancy_grid"))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    producto = input("Nombre: ")
    
    retorno = logic.req_1(control, producto)
    
    if retorno == False:
        print("No encontrado")
        return
    
    filas = []
    for llave in retorno:
        filas.append([llave, retorno[llave]])
    
    print(tabulate(filas, headers=["Requerimiento", "Resultado"], tablefmt="fancy_grid"))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    input_min = input("Ingrese el precio mínimo por caja: ")
    input_max = input("Ingrese el precio máximo por caja: ")
    
    retorno = logic.req_2(control, float(input_min), float(input_max))
    
    if retorno == False:
        print("No hay pedidos en el rango de precios")
        return
    encabezado=retorno.keys()
    filas=retorno.values()
    
    tabla_vertical=zip(encabezado, filas)
    
    print(tabulate(tabla_vertical, headers=["Requerimiento", "Resultado"], tablefmt="fancy_grid"))
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5}
    
    filtro = int(input("Ingrese el numero de el filtro que desea aplicar: \n1. 1.MAYOR\n2. 2.MENOR\n"))
    
        
    retorno = logic.req_5(catalog, filtro, producto, fecha_inicial, fecha_final)
        
    if retorno == False:
        print("No hay pedidos en el rango de precios")
        return
    encabezado=retorno.keys()
    filas=retorno.values()
        
    tabla_vertical=zip(encabezado, filas)
        
    print(tabulate(tabla_vertical, headers=["Requerimiento", "Resultado"], tablefmt="fancy_grid"))
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    fecha_inicio = input("Fecha inicial: ")
    fecha_fin = input("Fecha final: ")
    
    retorno = logic.req_6(control, fecha_inicio, fecha_fin)
    
    if retorno == False:
        print("No encontrado")
        return
    
    filas = []
    for llave in retorno:
        filas.append([llave, retorno[llave]])
    
    print(tabulate(filas, headers=["Requerimiento", "Resultado"], tablefmt="fancy_grid"))

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)