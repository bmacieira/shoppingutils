def check_availability(cart, inventory):
    disp=[]
    for item in cart:
        if inventory[item['produto']]==0:
            disp.append(False)
        else:
            disp.append(True)
    if False in disp:
        return False
    else:
        return True
