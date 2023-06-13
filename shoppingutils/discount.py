def apply_discount(cart, discount):
    #retira o % e devolve percentagem em valor decimal
    discount=int(discount[:-1])/100
    for item in cart:
        item['preco']=item['preco']-(item['preco']*discount)
    return cart
