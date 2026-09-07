def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def is_empty(my_list):
    is_empty=False
    if my_list["size"]==0:
        is_empty=True
    return is_empty

def size(my_list):
    return my_list["size"]

def add_first(my_list, element):
    node_nuevo= {"info": element, "next":None}
    
    if my_list["size"]==0:
        my_list["first"]=node_nuevo
        my_list["last"]=node_nuevo
    else:
        node_nuevo["next"]=my_list["first"]
        my_list["first"]=node_nuevo
    
    my_list["size"] +=1
    return my_list

def add_last(my_list, element):
    node_nuevo= {"info": element, "next":None}
    
    if my_list["size"]==0:
        my_list["first"]=node_nuevo
        my_list["last"]=node_nuevo
    else:
        my_list["last"]["next"]=node_nuevo
        my_list["last"]=node_nuevo
    
    my_list["size"] +=1
    return my_list

def first_element(my_list):
    return my_list["first"]["info"]

def last_element(my_list):
    return my_list["last"]["info"]

def get_element(my_list, pos):
    elemento = my_list["first"]
    for i in range(pos):
        elemento = elemento["next"]
    return elemento["info"]

def delete_element(my_list, pos):
    if my_list["size"]==1:
        my_list["first"]=None
        my_list["last"]=None
    else:
        if pos==0:
            my_list["first"]=my_list["first"]["next"]
        else:
            elemento_previo_borrar=my_list["first"]
            for i in range(pos-1):
                elemento_previo_borrar=elemento_previo_borrar["next"]
            elemento_previo_borrar["next"]=elemento_previo_borrar["next"]["next"]
            
            if pos==my_list["size"]-1:
                my_list["last"]=elemento_previo_borrar
    my_list["size"]-=1
    
    return my_list

def remove_first(my_list):
    elemento_eliminado = my_list['first']
    info_eliminada = elemento_eliminado['info']
    
    if my_list['size'] == 1:
        my_list['first'] = None
        my_list['last'] = None
    else:
        my_list['first'] = elemento_eliminado['next']
    
    elemento_eliminado['next'] = None
    my_list['size'] -= 1
    
    return info_eliminada

def remove_last(my_list):
    info_eliminada = my_list['last']['info']
    
    if my_list['size'] == 1:
        my_list['first'] = None
        my_list['last'] = None
    else:
        actual = my_list['first']
        while actual['next'] != my_list['last']:
            actual = actual['next']
        actual['next'] = None
        my_list['last'] = actual
    
    my_list['size'] -= 1
    return info_eliminada

def insert_element(my_list, element, pos):
    nuevo_nodo = {'info': element,
                  'next': None
                  }
    
    if pos == 0:
        nuevo_nodo['next'] = my_list['first']
        my_list['first'] = nuevo_nodo
        
        if my_list['size'] == 0:
            my_list['last'] = nuevo_nodo
    
    elif pos == my_list['size']:
        my_list['last']['next'] = nuevo_nodo
        my_list['last'] = nuevo_nodo
    
    else:
        actual = my_list['first']
        for nodo in range(pos - 1):
            actual = actual['next']
        
        nuevo_nodo['next'] = actual['next']
        actual['next'] = nuevo_nodo
    
    my_list['size'] +=1
    
    return my_list

def is_present(my_list, element, cmp_function):
    is_in_array=False
    temp=my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"])==0:
            is_in_array = True
        else:
            temp = temp["next"]
            count +=1
    
    if not is_in_array:
        count = -1
    return count

def change_info(my_list, pos, new_info):
    actual = my_list['first']
    for elemento in range(pos):
        actual = actual['next']
    
    actual['info'] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 != pos_2:
        actual = my_list['first']
        nodo_1 = None
        nodo_2 = None
        indice = 0
        
        while actual is not None:
            if indice == pos_1:
                nodo_1 = actual
            if indice == pos_2:
                nodo_2 = actual
            actual = actual['next']
            indice +=1
            
        nodo_1_info = nodo_1['info']
        nodo_1['info'] = nodo_2['info']
        nodo_2['info'] = nodo_1_info
    
    return my_list

def sub_list(my_list, pos_i, num_elements):
    sublista = new_list()
    elemento_actual = my_list['first']
    indice = 0
    elementos_agregados = 0
    
    while indice < pos_i:
        elemento_actual = elemento_actual['next']
        indice += 1
    
    while elementos_agregados < num_elements:
        add_last(sublista, elemento_actual['info'])
        elemento_actual = elemento_actual['next']
        elementos_agregados +=1
    
    return sublista