def new_stack():
    
    newstack = {
        "size": 0,
        "first": None,
        "last": None
    }

    return newstack

def push(my_stack, element):
    
    new_node = {"info": element, "next":my_stack["first"]} 
    
    if my_stack["size"] == 0:
        my_stack["first"] = new_node
        my_stack["last"] = new_node  
        
    my_stack["first"] = new_node
    my_stack["size"] += 1
    
    return my_stack

def pop(my_stack):
    if is_empty(my_stack):
        return None
    else:
        nodo_eliminado = my_stack['first']
        elemento_eliminado = nodo_eliminado['info']
        my_stack['first'] = nodo_eliminado['next']
        my_stack['size'] -= 1
        return elemento_eliminado

def is_empty(my_stack):
    return my_stack['size'] == 0

def top(my_stack):
    if is_empty(my_stack):
        return None
    else:
        return my_stack['first']['info']
    
def size(my_stack):
    return my_stack['size']