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
    
    chocolatefile = data_dir + "chocolate_sale_100_ptc.csv"
    input_file = csv.DictReader(open(chocolatefile, encoding='utf-8'))
    for order in input_file:
        arr.add_last(catalog['chocolate_sale'], order)
    
    end_time = get_time()
    total_time = delta_time(start_time, end_time)
    
    return catalog, total_time

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog, p_min, p_max):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    inicio=get_time()
    resultado={}
    pedidos=catalog["chocolate_sale"]
    
    pedidos_en_rango=sll.new_list()
    cantidad_pedidos_en_rango=0
    for i in range(arr.size(pedidos)):
        pedido=arr.get_element(pedidos, i)
        precio=float(pedido["Price_per_Box"])
        if precio >= p_min and precio <= p_max:
            cantidad_pedidos_en_rango += 1
            sll.add_last(pedidos_en_rango, pedido)
            
    resultado["cantidad_pedidos_en_rango"]=cantidad_pedidos_en_rango
    
    actual=pedidos_en_rango["first"]
    suma_discount=0
    suma_marketing=0
    suma_price=0
    mas_r=sll.first_element(pedidos_en_rango)
    
    
    while actual is not None:
        pedido=actual["info"]
        suma_discount += float(pedido["Discount_Pct"])
        suma_marketing += float(pedido["Marketing_Spend"])
        suma_price += float(pedido["Price_per_Box"])
        
        comparacion=sll.default_function(mas_r["Order_Date"], pedido["Order_Date"])
        
        if comparacion == -1:
            mas_r=pedido
            
        if comparacion == 0:
            c_amount=sll.default_function(float(mas_r["Amount"]), float(pedido["Amount"]))
            if c_amount == -1:
                mas_r=pedido
        actual=actual["next"]
        
        
    promedio_Discount_Pct=suma_discount/cantidad_pedidos_en_rango
    resultado["promedio_de_Discount_Pct"]=promedio_Discount_Pct
    
    promedio_Marketing_Spend=suma_marketing/cantidad_pedidos_en_rango
    resultado["promedio_de_Marketing_Spend"]=promedio_Marketing_Spend
    
    promedio_Price_per_Box=suma_price/cantidad_pedidos_en_rango
    resultado["promedio_de_Price_per_Box"]=promedio_Price_per_Box
    
    


    fin=get_time()
    tiempo_ejecucion=delta_time(inicio, fin)
    resultado["tiempo_ejecucion"]=tiempo_ejecucion
    return resultado


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


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

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
