def calculate_total_price(cart):
    total=0
    for item in cart:
        total+=item['preco']
    return total
