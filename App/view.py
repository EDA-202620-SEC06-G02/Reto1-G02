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
    
    print(f"\nTiempo de carga: {result['total_time']:.2f} ms")
    print(f"Total de pedidos cargados: {result['total_pedidos']}")
    
    print("\n--- Pedido de menor precio total ---")
    pmin = result["product_min"]
    print(f"Order_ID: {pmin['Order_ID']}")
    print(f"Producto: {pmin['Product']}")
    print(f"Pais: {pmin['Country']}")
    print(f"Canal: {pmin['Channel']}")
    print(f"Fecha: {pmin['Order_Date']}")
    print(f"Precio por caja: {pmin['Price_per_Box']}")
    print(f"Monto: {pmin['Amount']}")
    
    print("\n--- Pedido de mayor precio total ---")
    pmax = result["product_max"]
    print(f"Order_ID: {pmax['Order_ID']}")
    print(f"Producto: {pmax['Product']}")
    print(f"Pais: {pmax['Country']}")
    print(f"Canal: {pmax['Channel']}")
    print(f"Fecha: {pmax['Order_Date']}")
    print(f"Precio por caja: {pmax['Price_per_Box']}")
    print(f"Monto: {pmax['Amount']}")
    
    print("\n--- Primeros 5 registros cargados ---")
    for order in result["first_five"]["elements"]:
        print(f"{order['Order_ID']} | {order['Product']} | {order['Country']} | {order['Channel']} | {order['Order_Date']} | {order['Price_per_Box']} | {order['Amount']}")
    
    print("\n--- Ultimos 5 registros cargados ---")
    for order in result["last_five"]["elements"]:
        print(f"{order['Order_ID']} | {order['Product']} | {order['Country']} | {order['Channel']} | {order['Order_Date']} | {order['Price_per_Box']} | {order['Amount']}")
    
    
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
    
    print(f"\nTiempo de ejecucion: {retorno['total_time']:.2f} ms")
    print(f"Total de pedidos: {retorno['total_pedidos']}")
    
    print(f"\nPrecio por caja - promedio: {retorno['price_promedio']:.2f}, min: {retorno['price_min']}, max: {retorno['price_max']}")
    print(f"Descuento - promedio: {retorno['discount_promedio']:.2f}, min: {retorno['discount_min']}, max: {retorno['discount_max']}")
    print(f"Cajas enviadas - promedio: {retorno['boxes_promedio']:.2f}, min: {retorno['boxes_min']}, max: {retorno['boxes_max']}")
    print(f"Inversion en mercadeo - promedio: {retorno['marketing_promedio']:.2f}, min: {retorno['marketing_min']}, max: {retorno['marketing_max']}")
    print(f"\nAño con mas pedidos: {retorno['year_mas_pedidos']}")
    
    mayor = retorno["pedido_mayor_amount"]
    print("\n--- Pedido de mayor Amount ---")
    print(f"Order_ID: {mayor['Order_ID']}")
    print(f"Pais: {mayor['Country']}")
    print(f"Fecha: {mayor['Order_Date']}")
    print(f"Precio por caja: {mayor['Price_per_Box']}")
    print(f"Monto: {mayor['Amount']}")
    
    menor = retorno["pedido_menor_amount"]
    print("\n--- Pedido de menor Amount ---")
    print(f"Order_ID: {menor['Order_ID']}")
    print(f"Pais: {menor['Country']}")
    print(f"Fecha: {menor['Order_Date']}")
    print(f"Precio por caja: {menor['Price_per_Box']}")
    print(f"Monto: {menor['Amount']}")

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
    fecha_inicio = input("Fecha inicial: ")
    fecha_fin = input("Fecha final: ")
    
    retorno = logic.req_6(control, fecha_inicio, fecha_fin)
    
    if retorno == False:
        print("No encontrado")
        return
    
    print(f"\nTiempo de ejecucion: {retorno['total_time']:.2f} ms")
    print(f"Total de pedidos en el rango: {retorno['total_pedidos']}")
    
    print(f"\nCanal mas usado: {retorno['ruta_mas_usada']} ({retorno['ruta_mas_usada_pedidos']} pedidos, recaudo: {retorno['ruta_mas_usada_recaudo']:.2f})")
    print(f"Canal que mas recauda: {retorno['ruta_mas_recauda']} ({retorno['ruta_mas_recauda_pedidos']} pedidos, recaudo: {retorno['ruta_mas_recauda_recaudo']:.2f})")
    
    print("\n--- Reporte por canal ---")
    for canal in retorno["reporte_rutas"]["elements"]:
        print(f"\nCanal: {canal['channel']}")
        print(f"Total pedidos: {canal['total_pedidos']}")
        print(f"Total recaudo: {canal['total_recaudo']:.2f}")
        print(f"Precio promedio: {canal['price_promedio']:.2f}")
        print(f"Marketing promedio: {canal['marketing_promedio']:.2f}")
        
        pmax = canal["pedido_max"]
        if pmax is not None:
            print(f"Pedido mas costoso -> Order_ID: {pmax['Order_ID']}, Producto: {pmax['Product']}, Pais: {pmax['Country']}, Fecha: {pmax['Order_Date']}, Cajas: {pmax['Boxes_Shipped']}, Monto: {pmax['Amount']}")
        
        pmin = canal["pedido_min"]
        if pmin is not None:
            print(f"Pedido mas barato -> Order_ID: {pmin['Order_ID']}, Producto: {pmin['Product']}, Pais: {pmin['Country']}, Fecha: {pmin['Order_Date']}, Cajas: {pmin['Boxes_Shipped']}, Monto: {pmin['Amount']}")

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