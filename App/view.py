import sys
import App.logic as logic


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
    control = logic.load_data(control)
    return control

def print_req_0(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    country = input("Ingrese el País: ")
    channel = input("Ingrese el Canal (Retail, Online, Wholesale): ")

    result = logic.req_3(control, country, channel)

    print("\n" + "="*40)
    print(" RESULTADOS DEL REQUERIMIENTO 3")
    print("="*40)
    print(f"Tiempo de ejecución: {result['execution_time']:.3f} ms")
    print(f"Total de pedidos encontrados: {result['count']}")
    
    if result['count'] > 0:
        print(f"Promedio de Precio por Caja: ${result['avg_price']:.2f}")
        print(f"Promedio de Descuento: {result['avg_discount']:.2f}%")
        print(f"Promedio de Inversión en Mercadeo: ${result['avg_marketing']:.2f}")
        print(f"Promedio de Cajas Enviadas: {result['avg_boxes']:.2f}")
        print(f"Producto más frecuente: {result['most_frequent_product']}")
        print(f"Año con más pedidos: {result['most_frequent_year']}")
    else:
        print("No se encontraron registros para la combinación especificada.")
    print("="*40 + "\n")
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    product = input("Ingrese el Producto: ").strip().title()
    country = input("Ingrese el País: ").strip().title()

    result = logic.req_4(control, product, country)

    print("\n" + "="*50)
    print(" RESULTADOS DEL REQUERIMIENTO 4")
    print("="*50)
    print(f"Tiempo de ejecución: {result['execution_time']:.3f} ms")
    print(f"Total de pedidos encontrados: {result['count']}")

    if result['count'] > 0:
        print(f"Promedio de Precio por Caja: ${result['avg_price']:.2f}")
        print(f"Promedio de Descuento: {result['avg_discount']:.2f}%")
        print(f"Promedio de Inversión en Mercadeo: ${result['avg_marketing']:.2f}")
        print(f"Promedio de Cajas Enviadas: {result['avg_boxes']:.2f}")
        
        print("\n--- Top 2 Pedidos con mayor Amount ---")
        for idx, order in enumerate(result['top_orders'], 1):
            print(f"\n[Pedido #{idx}]")
            print(f"  ID Pedido: {order['Order_ID']}")
            print(f"  Canal: {order['Channel']}")
            print(f"  Fecha: {order['Order_Date']}")
            print(f"  Cajas Enviadas: {order['Boxes_Shipped']}")
            print(f"  Monto (Amount): ${order['Amount']:.2f}")
    else:
        print("No se encontraron registros para la combinación especificada.")
    print("="*50 + "\n")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

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

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)