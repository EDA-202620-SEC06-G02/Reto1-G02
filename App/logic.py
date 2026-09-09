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
        comparacion_r = None
        comparacion_mayor_a = None
        comparacion_menor_a = None
        
        if pedido["Order_Date"] > mas_r["Order_Date"]:
            comparacion_r= -1
        elif pedido["Order_Date"] == mas_r["Order_Date"]:
            comparacion_r=0
       
        if float(pedido["Amount"]) > float(mayor_a["Amount"]):
            comparacion_mayor_a=-1
        elif float(pedido["Amount"]) == float(mayor_a["Amount"]):
            comparacion_mayor_a=0
            
        
        if float(pedido["Amount"]) < float(menor_a["Amount"]):
            comparacion_menor_a=1
        elif float(pedido["Amount"]) == float(menor_a["Amount"]):
            comparacion_menor_a=0
        
        if comparacion_r == -1:
            mas_r=pedido
            
        if comparacion_r == 0:
            if float(pedido["Amount"]) > float(mas_r["Amount"]):
                mas_r = pedido
                
        if comparacion_mayor_a == -1:
            mayor_a=pedido
        
        
        if comparacion_mayor_a == 0:
            if float(mayor_a["Price_per_Box"]) > float(pedido["Price_per_Box"]):
                mayor_a = pedido
                
        if comparacion_menor_a == 1:
                    menor_a=pedido
                    
        
        if comparacion_menor_a == 0:
            if float(menor_a["Price_per_Box"]) > float(pedido["Price_per_Box"]):
                menor_a = pedido
                
        actual=actual["next"]
        
        
    promedio_Discount_Pct=suma_discount/cantidad_pedidos_en_rango
    resultado["promedio_de_Discount_Pct"]=promedio_Discount_Pct
    
    promedio_Marketing_Spend=suma_marketing/cantidad_pedidos_en_rango
    resultado["promedio_de_Marketing_Spend"]=promedio_Marketing_Spend
    
    promedio_Price_per_Box=suma_price/cantidad_pedidos_en_rango
    resultado["promedio_de_Price_per_Box"]=promedio_Price_per_Box
    
    mas_r_final = (f"Producto: {mas_r['Product']}\n"
                 f"Pais: {mas_r['Country']}\n"
                 f"Canal: {mas_r['Channel']}\n"
                 f"Fecha: {mas_r['Order_Date']}\n"
                 f"Precio por caja: {mas_r['Price_per_Box']}\n"
                 f"Monto: {mas_r['Amount']}\n"
    )
    resultado["pedido_mas_reciente"]=mas_r_final
    
    mayor_precio_final = (f"Producto: {mayor_a['Product']}\n"
                     f"Pais: {mayor_a['Country']}\n"
                     f"Canal: {mayor_a['Channel']}\n"
                     f"Fecha: {mayor_a['Order_Date']}\n"
                     f"Precio por caja: {mayor_a['Price_per_Box']}\n"
                     f"Monto: {mayor_a['Amount']}\n"
                     )
    resultado["pedido_mayor_precio_total"]=mayor_precio_final
    
    menor_precio_final = (f"Producto: {menor_a["Product"]}\n"
                     f"Pais: {menor_a["Country"]}\n"
                     f"Canal: {menor_a["Channel"]}\n"
                     f"Fecha: {menor_a["Order_Date"]}\n"
                     f"Precio por caja: {menor_a["Price_per_Box"]}\n"
                     f"Monto: {menor_a["Amount"]}\n"
    )
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
