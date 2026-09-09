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
            
    if sll.size(pedidos_en_rango) == 0:
            return False
        
    resultado["cantidad_pedidos_en_rango"]=cantidad_pedidos_en_rango
    
    actual=pedidos_en_rango["first"]
    suma_discount=0
    suma_marketing=0
    suma_price=0
    mas_r=sll.first_element(pedidos_en_rango)
    mayor_a=sll.first_element(pedidos_en_rango)
    menor_a=sll.first_element(pedidos_en_rango)
    
    
    while actual is not None:
        pedido=actual["info"]
        suma_discount += float(pedido["Discount_Pct"])
        suma_marketing += float(pedido["Marketing_Spend"])
        suma_price += float(pedido["Price_per_Box"])
        
        comparacion_r=sll.default_function(mas_r["Order_Date"], pedido["Order_Date"])
        comparacion_mayor_a=sll.default_function(float(mayor_a["Amount"]), float(pedido["Amount"]))
        comparacion_menor_a=sll.default_function(float(menor_a["Amount"]), float(pedido["Amount"]))
        
        if comparacion_r == -1:
            mas_r=pedido
            
        if comparacion_r == 0:
            c_amount=sll.default_function(float(mas_r["Amount"]), float(pedido["Amount"]))
            if c_amount == -1:
                mas_r=pedido
                
        if comparacion_mayor_a == -1:
            mayor_a=pedido
                    
        if comparacion_mayor_a == 0:
            c_amount=sll.default_function(float(mayor_a["Price_per_Box"]), float(pedido["Price_per_Box"]))
            if c_amount == 1:
                mayor_a=pedido
                
        if comparacion_menor_a == 1:
                    menor_a=pedido
                    
        if comparacion_menor_a == 0:
            c_amount=sll.default_function(float(menor_a["Price_per_Box"]), float(pedido["Price_per_Box"]))
            if c_amount == 1:
                menor_a=pedido
                
        actual=actual["next"]
        
        
    promedio_Discount_Pct=suma_discount/cantidad_pedidos_en_rango
    resultado["promedio_de_Discount_Pct"]=promedio_Discount_Pct
    
    promedio_Marketing_Spend=suma_marketing/cantidad_pedidos_en_rango
    resultado["promedio_de_Marketing_Spend"]=promedio_Marketing_Spend
    
    promedio_Price_per_Box=suma_price/cantidad_pedidos_en_rango
    resultado["promedio_de_Price_per_Box"]=promedio_Price_per_Box
    
    mas_r_final = {"Producto":mas_r["Product"],
                 "Pais":mas_r["Country"],
                 "Canal":mas_r["Channel"],
                 "Fecha":mas_r["Order_Date"],
                 "Precio por caja":mas_r["Price_per_Box"],
                 "Monto":mas_r["Amount"]
                 }
    resultado["pedido_mas_reciente"]=mas_r_final
    
    mayor_precio_final = {"Producto":mayor_a["Product"],
                     "Pais":mayor_a["Country"],
                     "Canal":mayor_a["Channel"],
                     "Fecha":mayor_a["Order_Date"],
                     "Precio por caja":mayor_a["Price_per_Box"],
                     "Monto":mayor_a["Amount"]
                     }
    resultado["pedido_mayor_precio_total"]=mayor_precio_final
    
    menor_precio_final = {"Producto":menor_a["Product"],
                     "Pais":menor_a["Country"],
                     "Canal":menor_a["Channel"],
                     "Fecha":menor_a["Order_Date"],
                     "Precio por caja":menor_a["Price_per_Box"],
                     "Monto":menor_a["Amount"]
                     }
    resultado["pedido_menor_precio_total"]=menor_precio_final



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
