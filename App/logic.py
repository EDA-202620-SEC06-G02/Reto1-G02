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
    
    #Variables de carga
    product_min = None
    product_max = None
    first_five = arr.new_list()
    last_five = queue.new_queue()
    
    chocolatefile = data_dir + "chocolate_sale_15_elements.csv"
    input_file = csv.DictReader(open(chocolatefile, encoding='utf-8'))
    for order in input_file:
        arr.add_last(catalog['chocolate_sale'], order)
        
        #Calcular producto con el menor precio
        if (product_min is None) or (order["Amount"] < product_min["Amount"]):
            product_min = order
        
        #Calcular producto con el mayor precio
        if (product_max is None) or (order["Amount"] > product_max["Amount"]):
            product_max = order
            
        #Calcular primeras 5
        if catalog["chocolate_sale"]["size"] < 5:
            arr.add_last(first_five)
            
        #Calcular ultimas 5 con QUEUE
        queue.enqueue(last_five, order)
        if queue.size(last_five) > 5:
            queue.dequeue(last_five)
    
    #Total de pedidos cargados
    total_pedidos = catalog["chocolate_sale"]["size"]
    
    end_time = get_time()
    total_time = delta_time(start_time, end_time)
    
    return {"total_time": total_time,
            "total_pedidos": total_pedidos,
            "product_min": product_min,
            "product_max": product_max,
            "first_five": first_five,
            "last_five": last_five}

# Funciones de consulta sobre el catálogo
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
