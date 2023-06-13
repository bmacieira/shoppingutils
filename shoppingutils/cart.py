def calculate_total_price(cart):
    '''
    :param cart: dict
    :return: sum of value of all items
    '''
    total=0
    for item in cart:
        total+=item['preco']
    return total
