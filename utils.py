from config import *




def get_products():
    "Fetch Stripe Products To Our Models"

    # PULL PRODUCTS TO A LIST
    response = stripe.Product.list(limit=50)
    products = list(response['data'])
    return products


def get_product(data, id):
    length = len(data)

    index = id + 1

    if index > length:
        index = 0
    
    else:
        pass

    return data[id], index
    

def get_next_product(data, id):   
    if id <= 0 or id >= len(data):
        index = 0
    else:
        index = id + 1

    return data[id], index



def get_prev_product(data, id):
    if id <= 0 or id >= len(data):
        index = 0
    else:
        index = id - 1

    return data[id], index


