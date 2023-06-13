# ShoppingUtils

O package ShoppingUtils disponibiliza uma 
série de  funcionalidades que facilitam a
gestão de compras de clientes.

Requer um inventório com o formato:<br>
inventory={'produto'(str):quantidade(int),...}<br>

Requer um carro de compras com o formato:<br>
cart=[{'produto':'descricao'(str), 'preco':valor(int)},...]

<b>File: cart.py</b>

calculate_total_price(cart)

#Calcula o total do carro de compras

<b>File: discount.py</b>

apply_discount(cart, discount(str))<br>
ex: discount = '10%'

#Devolve o carro de compras com os valores atualizados com desconto

<b>File: inventory.py</b>

check_availability(cart, inventory)<br>

#Verifica a dispobilidade de todos os items
Em caso de algum item indisponível devolve False
Caso todos os items disponíveis devolve True