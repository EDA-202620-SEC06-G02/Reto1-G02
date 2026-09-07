def new_queue():
    
    newqueue = {
        "elements": [],
        "size" : 0
    }
    
    return newqueue

def enqueue(my_queue, element):
    
    my_queue["elements"].append(element)
    my_queue["size"] += 1
    
    return my_queue

def dequeue(my_queue):
    if is_empty(my_queue):
        return None
    else:
        elemento_eliminado = my_queue['elements'].pop(0)
        my_queue["size"] -= 1
        return elemento_eliminado

def peek(my_queue):
    if is_empty(my_queue):
        return None
    else:
        return my_queue['elements'][0]

def is_empty(my_queue):
    return my_queue['size'] == 0

def size(my_queue):
    return my_queue['size']