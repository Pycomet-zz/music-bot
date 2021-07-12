from config import *


def payment_status(id):
    "Confirm payment session"

    response = stripe.checkout.Session.retrieve(id)
    status = response['payment_status']

    if status == "unpaid":
        return False
    else:
        import pdb; pdb.set_trace()
        return True


def buy_product(product, price_id):
    "Create Session & Return Url"

    result = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        payment_method_types=["card"],
        line_items=[
        {
            "price": price_id,
            "quantity": 1,
        },
        ],
        mode="payment",
    )

    return result['url'], result['id']


def get_products():
    "Fetch Stripe Products To Our Models"

    products = []
    # PULL PRODUCTS TO A LIST
    prices = stripe.Price.list(limit=50)

    for price in prices['data']:
        product = stripe.Product.retrieve(price['product'])
        product.update({'price_id': price['id']})

        products.append(product)
        
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
    fig = len(data) - 1   
    if id == fig:
        index = 1
    else:
        index = id + 1

    return data[id], index



def get_prev_product(data, id):
    if id == 1:
        index = len(data) - 1
    else:
        index = id - 1

    return data[id], index


