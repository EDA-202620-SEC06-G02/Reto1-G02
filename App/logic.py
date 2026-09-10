import time
import csv
import os

#Importacion de estructuras de datos
from DataStructures.List import array_list as arr
from DataStructures.List import single_linked_list as sll
from DataStructures.Stack import stack
from DataStructures.Queue import queue

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {"chocolate_sale":None}
    catalog["chocolate_sale"] = arr.new_list()
    return catalog

# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    
    chocolatefile = data_dir + "chocolate_sale_15_elements.csv"
    input_file = csv.DictReader(open(chocolatefile, encoding='utf-8'))
    for order in input_file:
        arr.add_last(catalog['chocolate_sale'], order)
    
    end_time = get_time()
    total_time = delta_time(start_time, end_time)
    
    return catalog, total_time

# Funciones de consulta sobre el catálogo
def req_0(catalog, total_time):
    """
    Retorna el resultado del requerimiento Carga de Datos
    """
    # TODO: Modificar el requerimiento Carga de Datos
    pass

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog, filtro, producto, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    inicio = get_time()
    resultado = {}
    if filtro == 1:
        filtro = "MAYOR"
    
    if filtro == 2:
        filtro = "MENOR"
        
    resultado["Filtro"] = filtro
    pedidos=catalog["chocolate_sale"]
    
    
    pedidos_en_rango_f=sll.new_list()
    cantidad_pedidos_en_rango_f=0
    
    suma_price = 0.0
    suma_boxes = 0.0
    suma_marketing = 0.0
    for i in range(arr.size(pedidos)):
        pedido=arr.get_element(pedidos, i)
        if pedido["Product"] == producto:
            fecha=pedido["Order_Date"]
            if fecha >= fecha_inicial and fecha <= fecha_final:
                cantidad_pedidos_en_rango_f += 1
                sll.add_last(pedidos_en_rango_f, pedido)
                suma_price += float(pedido["Price_per_Box"])
                suma_boxes += float(pedido["Boxes_Shipped"])
                suma_marketing += float(pedido["Marketing_Spend"])

    if sll.size(pedidos_en_rango_f) == 0:
        return False
    
    resultado["cantidad_pedidos_en_rango_fecha"]=cantidad_pedidos_en_rango_f
    resultado["promedio_price"]=suma_price/cantidad_pedidos_en_rango_f
    resultado["promedio_boxes"]=suma_boxes/cantidad_pedidos_en_rango_f
    resultado["promedio_marketing"]=suma_marketing/cantidad_pedidos_en_rango_f

    actual=pedidos_en_rango_f["first"]
    
    mayor=sll.first_element(pedidos_en_rango_f)
    menor=sll.first_element(pedidos_en_rango_f)
            
    if filtro == "MAYOR":
        while actual is not None:
            pedido=actual["info"]
            
            if float(pedido["Amount"]) > float(mayor["Amount"]):
                mayor=pedido
            elif float(pedido["Amount"]) == float(mayor["Amount"]):
                if float(pedido["Price_per_Box"]) < float(mayor["Price_per_Box"]):
                    mayor=pedido
                elif float(pedido["Price_per_Box"]) == float(mayor["Price_per_Box"]):
                    if float(pedido["Marketing_Spend"]) < float(mayor["Marketing_Spend"]):
                        mayor=pedido
            
            actual=actual["next"]
        mayor_final = (f"Precio por caja: {mayor['Price_per_Box']}\n"
                       f"Cajas enviadas: {mayor['Boxes_Shipped']}\n"
                       f"Monto: {mayor['Amount']}\n"
                       f"Canal: {mayor['Channel']}\n"
                       f"Fecha: {mayor['Order_Date']}\n"
                       f"Inversión en mercadeo: {mayor['Marketing_Spend']}\n"
                       )
        resultado["pedido_mayor_amount"]=mayor_final
    
    if filtro == "MENOR":
        while actual is not None:
            pedido=actual["info"]
                
            if float(pedido["Amount"]) < float(menor["Amount"]):
                menor=pedido
            elif float(pedido["Amount"]) == float(menor["Amount"]):
                if float(pedido["Price_per_Box"]) < float(menor["Price_per_Box"]):
                    menor=pedido
                elif float(pedido["Price_per_Box"]) == float(menor["Price_per_Box"]):
                    if float(pedido["Marketing_Spend"]) < float(menor["Marketing_Spend"]):
                        menor=pedido

                
            actual=actual["next"]
        menor_final = (f"Precio por caja: {menor['Price_per_Box']}\n"
                       f"Cajas enviadas: {menor['Boxes_Shipped']}\n"
                       f"Monto: {menor['Amount']}\n"
                       f"Canal: {menor['Channel']}\n"
                       f"Fecha: {menor['Order_Date']}\n"
                       f"Inversión en mercadeo: {menor['Marketing_Spend']}\n"
                       )
        resultado["pedido_menor_amount"]=menor_final

    
    final = get_time()
    tiempo_final = delta_time(inicio, final)
    resultado["Tiempo"] = tiempo_final
    
    return resultado

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
