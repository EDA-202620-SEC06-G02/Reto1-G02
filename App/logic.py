import time
import csv
import os

#Importacion de estructuras de datos
from DataStructures.List import array_list as arr
from DataStructures.List import single_linked_list as sll
from DataStructures.Stack import stack
from DataStructures.Queue import queue

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

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
    
    chocolatefile = data_dir + "chocolate_sale_20_ptc.csv"
    input_file = csv.DictReader(open(chocolatefile, encoding='utf-8-sig'))
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

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {"chocolate_sale":None}
    catalog["chocolate_sale"] = arr.new_list()
    return catalog

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


def req_3(catalog, country, channel):
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

        if order['Country'] == country and order['Channel'] == channel:
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
