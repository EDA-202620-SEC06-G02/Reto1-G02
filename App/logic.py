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
        
        #Caso Unknow
        for campo in ["Order_ID", "Product", "Country", "Channel", "Order_Date", "Price_per_Box", "Amount"]:
            if order[campo] is None or order[campo].strip() == "":
                order[campo] = "Unknown"
        
        #Calcular producto con el menor precio
        if order["Amount"] != "Unknown":
            if (product_min is None) or (product_min["Amount"] == "Unknown") or (float(order["Amount"]) < float(product_min["Amount"])):
                product_min = order
            elif float(order["Amount"]) == float(product_min["Amount"]):
                if order["Price_per_Box"] != "Unknown" and float(order["Price_per_Box"]) < float(product_min["Price_per_Box"]):
                    product_min = order
        
        #Calcular producto con el mayor precio
        if order["Amount"] != "Unknown":
            if (product_max is None) or (product_max["Amount"] == "Unknown") or (float(order["Amount"]) > float(product_max["Amount"])):
                product_max = order
            elif float(order["Amount"]) == float(product_max["Amount"]):
                if order["Price_per_Box"] != "Unknown" and float(order["Price_per_Box"]) < float(product_max["Price_per_Box"]):
                    product_max = order
            
        #Calcular primeras 5
        if catalog["chocolate_sale"]["size"] < 5:
            arr.add_last(first_five, order)
            
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
def req_1(catalog, producto):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    
    total_pedidos = 0
    
    suma_price = 0
    price_min = None
    price_max = None
    
    suma_discount = 0
    discount_min = None
    discount_max = None
    
    suma_boxes = 0
    boxes_min = None
    boxes_max = None
    
    suma_marketing = 0
    marketing_min = None
    marketing_max = None
    
    years = {}
    
    pedido_mayor_amount = None
    pedido_menor_amount = None
    
    pedidos_producto = sll.new_list()
    
    for i in range(arr.size(catalog["chocolate_sale"])):
        order = arr.get_element(catalog["chocolate_sale"], i)
        if order["Product"] == producto:
            sll.add_last(pedidos_producto, order)
    
    for i in range(sll.size(pedidos_producto)):
        order = sll.get_element(pedidos_producto, i)
        
        total_pedidos += 1
        
        price = float(order["Price_per_Box"])
        suma_price += price
        if price_min is None or price < price_min:
            price_min = price
        if price_max is None or price > price_max:
            price_max = price
        
        discount = float(order["Discount_Pct"])
        suma_discount += discount
        if discount_min is None or discount < discount_min:
            discount_min = discount
        if discount_max is None or discount > discount_max:
            discount_max = discount
        
        boxes = float(order["Boxes_Shipped"])
        suma_boxes += boxes
        if boxes_min is None or boxes < boxes_min:
            boxes_min = boxes
        if boxes_max is None or boxes > boxes_max:
            boxes_max = boxes
        
        marketing = float(order["Marketing_Spend"])
        suma_marketing += marketing
        if marketing_min is None or marketing < marketing_min:
            marketing_min = marketing
        if marketing_max is None or marketing > marketing_max:
            marketing_max = marketing
        
        year = order["Order_Date"].split("-")[0] #Linea de error #Comando utilizado para extraer el año de la fecha
        if year in years:
            years[year] += 1
        else:
            years[year] = 1
        
        amount = float(order["Amount"])
        if (pedido_mayor_amount is None) or (amount > float(pedido_mayor_amount["Amount"])):
            pedido_mayor_amount = order
        elif amount == float(pedido_mayor_amount["Amount"]):
            if marketing < float(pedido_mayor_amount["Marketing_Spend"]):
                pedido_mayor_amount = order
        
        if (pedido_menor_amount is None) or (amount < float(pedido_menor_amount["Amount"])):
            pedido_menor_amount = order
        elif amount == float(pedido_menor_amount["Amount"]):
            if marketing < float(pedido_menor_amount["Marketing_Spend"]):
                pedido_menor_amount = order
    
    year_mas_pedidos = None
    max_pedidos_year = 0
    for year in years:
        if years[year] > max_pedidos_year:
            max_pedidos_year = years[year]
            year_mas_pedidos = year

    if total_pedidos > 0:
        promedio_price = suma_price / total_pedidos
        promedio_discount = suma_discount / total_pedidos
        promedio_boxes = suma_boxes / total_pedidos
        promedio_marketing = suma_marketing / total_pedidos
    else:
        promedio_price = 0
        promedio_discount = 0
        promedio_boxes = 0
        promedio_marketing = 0
    
    end_time = get_time()
    total_time = delta_time(start_time, end_time)
    
    return {"total_time": total_time,
            "total_pedidos": total_pedidos,
            "price_promedio": promedio_price,
            "price_min": price_min,
            "price_max": price_max,
            "discount_promedio": promedio_discount,
            "discount_min": discount_min,
            "discount_max": discount_max,
            "boxes_promedio": promedio_boxes,
            "boxes_min": boxes_min,
            "boxes_max": boxes_max,
            "marketing_promedio": promedio_marketing,
            "marketing_min": marketing_min,
            "marketing_max": marketing_max,
            "year_mas_pedidos": year_mas_pedidos,
            "pedido_mayor_amount": pedido_mayor_amount,
            "pedido_menor_amount": pedido_menor_amount}

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


def req_6(catalog, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    
    total_pedidos = 0
    
    ruta_data = {}
    ruta_lista = arr.new_list()
    
    for i in range(arr.size(catalog["chocolate_sale"])):
        order = arr.get_element(catalog["chocolate_sale"], i)
        
        for campo in ["Channel", "Amount", "Price_per_Box", "Marketing_Spend", "Order_ID", "Product", "Country", "Order_Date", "Boxes_Shipped"]:
            if order[campo] is None or order[campo].strip() == "":
                order[campo] = "Unknown"
        
        if order["Order_Date"] != "Unknown" and order["Order_Date"] >= fecha_inicio and order["Order_Date"] <= fecha_fin:
            total_pedidos += 1
            
            channel = order["Channel"]
            
            if channel not in ruta_data:
                arr.add_last(ruta_lista, channel)
                ruta_data[channel] = {
                    "count": 0,
                    "suma_amount": 0,
                    "suma_price": 0,
                    "suma_marketing": 0,
                    "count_price": 0,
                    "count_marketing": 0,
                    "pedido_max": None,
                    "pedido_min": None
                }
            
            ruta_data[channel]["count"] += 1
            
            if order["Amount"] != "Unknown":
                amount = float(order["Amount"])
                ruta_data[channel]["suma_amount"] += amount
                
                if ruta_data[channel]["pedido_max"] is None or amount > float(ruta_data[channel]["pedido_max"]["Amount"]):
                    ruta_data[channel]["pedido_max"] = order
                
                if ruta_data[channel]["pedido_min"] is None or amount < float(ruta_data[channel]["pedido_min"]["Amount"]):
                    ruta_data[channel]["pedido_min"] = order
            
            if order["Price_per_Box"] != "Unknown":
                ruta_data[channel]["suma_price"] += float(order["Price_per_Box"])
                ruta_data[channel]["count_price"] += 1
            
            if order["Marketing_Spend"] != "Unknown":
                ruta_data[channel]["suma_marketing"] += float(order["Marketing_Spend"])
                ruta_data[channel]["count_marketing"] += 1
    
    ruta_mas_usada = None
    max_pedidos_ruta = 0
    
    ruta_mas_recauda = None
    max_recaudo_ruta = 0
    
    for i in range(arr.size(ruta_lista)):
        channel = arr.get_element(ruta_lista, i)
        
        if ruta_data[channel]["count"] > max_pedidos_ruta:
            max_pedidos_ruta = ruta_data[channel]["count"]
            ruta_mas_usada = channel
        
        if ruta_data[channel]["suma_amount"] > max_recaudo_ruta:
            max_recaudo_ruta = ruta_data[channel]["suma_amount"]
            ruta_mas_recauda = channel
    
    reporte_rutas = arr.new_list()
    for i in range(arr.size(ruta_lista)):
        channel = arr.get_element(ruta_lista, i)
        data = ruta_data[channel]
        
        if data["count_price"] > 0:
            promedio_price = data["suma_price"] / data["count_price"]
        else:
            promedio_price = 0
        
        if data["count_marketing"] > 0:
            promedio_marketing = data["suma_marketing"] / data["count_marketing"]
        else:
            promedio_marketing = 0
        
        arr.add_last(reporte_rutas, {
            "channel": channel,
            "total_pedidos": data["count"],
            "total_recaudo": data["suma_amount"],
            "price_promedio": promedio_price,
            "marketing_promedio": promedio_marketing,
            "pedido_max": data["pedido_max"],
            "pedido_min": data["pedido_min"]
        })
    
    end_time = get_time()
    total_time = delta_time(start_time, end_time)
    
    return {"total_time": total_time,
            "total_pedidos": total_pedidos,
            "ruta_mas_usada": ruta_mas_usada,
            "ruta_mas_usada_pedidos": max_pedidos_ruta,
            "ruta_mas_usada_recaudo": ruta_data[ruta_mas_usada]["suma_amount"] if ruta_mas_usada else 0,
            "ruta_mas_recauda": ruta_mas_recauda,
            "ruta_mas_recauda_pedidos": ruta_data[ruta_mas_recauda]["count"] if ruta_mas_recauda else 0,
            "ruta_mas_recauda_recaudo": max_recaudo_ruta,
            "reporte_rutas": reporte_rutas}

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
