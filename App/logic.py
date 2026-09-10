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
    
    chocolatefile = data_dir + "chocolate_sale_100_elementos.csv"
    input_file = csv.DictReader(open(chocolatefile, encoding='utf-8'))
    for order in input_file:
        
        # --- CONVERSIÓN DE TIPOS ---
        
        order['Order_ID'] = order['Order_ID'] if order['Order_ID'] else "Unknown"
        order['Product'] = order['Product'] if order['Product'] else "Unknown"
        order['Country'] = order['Country'] if order['Country'] else "Unknown"
        order['Channel'] = order['Channel'] if order['Channel'] else "Unknown"
        order['Order_Date'] = order['Order_Date'] if order['Order_Date'] else "Unknown"
        
        order['Discount_Pct'] = float(order['Discount_Pct']) if order['Discount_Pct'] else 0.0
        order['Price_per_Box'] = float(order['Price_per_Box']) if order['Price_per_Box'] else 0.0
        order['Marketing_Spend'] = float(order['Marketing_Spend']) if order['Marketing_Spend'] else 0.0
        order['Amount'] = float(order['Amount']) if order['Amount'] else 0.0
        
        order['Boxes_Shipped'] = int(order['Boxes_Shipped']) if order['Boxes_Shipped'] else 0
        
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


def req_3(catalog, Country, Channel):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    
    start_time = get_time()
    
    sales_list = catalog['chocolate_sale']
    total_elements = arr.size(sales_list)

    count = 0
    sum_price = 0.0
    sum_discount = 0.0
    sum_marketing = 0.0
    sum_boxes = 0

    product_counts = {}
    year_counts = {}
    
    for i in range(total_elements):
        order = arr.get_element(sales_list, i)

        if order['Country'] == Country and order['Channel'] == Channel:
            count += 1
            sum_price += order['Price_per_Box']
            sum_discount += order['Discount_Pct']
            sum_marketing += order['Marketing_Spend']
            sum_boxes += order['Boxes_Shipped']

            prod = order['Product']
            product_counts[prod] = product_counts.get(prod, 0) + 1

            date_str = str(order['Order_Date'])
            year = date_str.split('-')[0]
            year_counts[year] = year_counts.get(year, 0) + 1
            
    end_time = get_time()
    execution_time = delta_time(start_time, end_time)
    
    if count == 0:
        return {
            "execution_time": execution_time,
            "count": 0,
            "avg_price": 0.0,
            "avg_discount": 0.0,
            "avg_marketing": 0.0,
            "avg_boxes": 0.0,
            "most_frequent_product": "Unknown",
            "most_frequent_year": "Unknown"
        }
    
    avg_price = sum_price / count
    avg_discount = sum_discount / count
    avg_marketing = sum_marketing / count
    avg_boxes = sum_boxes / count

    most_frequent_product = max(product_counts, key=product_counts.get)
    most_frequent_year = max(year_counts, key=year_counts.get)

    return {
        "execution_time": execution_time,
        "count": count,
        "avg_price": avg_price,
        "avg_discount": avg_discount,
        "avg_marketing": avg_marketing,
        "avg_boxes": avg_boxes,
        "most_frequent_product": most_frequent_product,
        "most_frequent_year": most_frequent_year
    }


def req_4(catalog, product, country):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    
    start_time = get_time()
        
    sales_list = catalog['chocolate_sale']
    total_elements = arr.size(sales_list)
        
    count = 0
    sum_price = 0.0
    sum_discount = 0.0
    sum_marketing = 0.0
    sum_boxes = 0
    
    amount_1 = None
    amount_2 = None
    
    def is_better(order_a, order_b):
        """
        Retorna True si order_a tiene mayor Amount
        
        """
        if order_b is None:
            return True

        if order_a['Amount'] > order_b['Amount']:
            return True
        elif order_a['Amount'] < order_b['Amount']:
            return False

        if order_a['Marketing_Spend'] < order_b['Marketing_Spend']:
            return True
        elif order_a['Marketing_Spend'] > order_b['Marketing_Spend']:
            return False

        return order_a['Order_ID'] < order_b['Order_ID']
    
    for i in range(total_elements):
        order = arr.get_element(sales_list, i)

        if order['Product'] == product and order['Country'] == country:
            count += 1
            sum_price += order['Price_per_Box']
            sum_discount += order['Discount_Pct']
            sum_marketing += order['Marketing_Spend']
            sum_boxes += order['Boxes_Shipped']

            if is_better(order, top_1):
                top_2 = top_1
                top_1 = order
            elif is_better(order, top_2):
                top_2 = order
                
    end_time = get_time()
    execution_time = delta_time(start_time, end_time)

    if count == 0:
        return {
            "execution_time": execution_time,
            "count": 0,
            "avg_price": 0.0,
            "avg_discount": 0.0,
            "avg_marketing": 0.0,
            "avg_boxes": 0.0,
            "top_orders": []
        }

    avg_price = sum_price / count
    avg_discount = sum_discount / count
    avg_marketing = sum_marketing / count
    avg_boxes = sum_boxes / count

    top_orders = arr.new_list()

    if amount_1 is not None:
        order_dict_1 = {
            "Order_ID": amount_1["Order_ID"],
            "Channel": amount_1["Channel"],
            "Order_Date": amount_1["Order_Date"],
            "Boxes_Shipped": amount_1["Boxes_Shipped"],
            "Amount": amount_1["Amount"]
        }
        arr.add_last(top_orders, order_dict_1)

    if amount_2 is not None:
        order_dict_2 = {
            "Order_ID": amount_2["Order_ID"],
            "Channel": amount_2["Channel"],
            "Order_Date": amount_2["Order_Date"],
            "Boxes_Shipped": amount_2["Boxes_Shipped"],
            "Amount": amount_2["Amount"]
        }
        arr.add_last(top_orders, order_dict_2)
    
    return {
        "execution_time": execution_time,
        "count": count,
        "avg_price": avg_price,
        "avg_discount": avg_discount,
        "avg_marketing": avg_marketing,
        "avg_boxes": avg_boxes,
        "top_orders": top_orders
    }

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
