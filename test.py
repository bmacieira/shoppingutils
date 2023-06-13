from shoppingutils.cart import calculate_total_price
from shoppingutils.discount import apply_discount
from shoppingutils.inventory import check_availability

inventory={'pao':10, 'manteiga':1, 'bolachas':6}
cart=[{'produto':'pao', 'preco':1.43}, {'produto':'manteiga', 'preco':2.19}, {'produto':'bolachas', 'preco':2.00}]

print(calculate_total_price(cart))
print(apply_discount(cart, '10%'))
print(check_availability(cart, inventory))

