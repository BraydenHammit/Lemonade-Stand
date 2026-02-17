import random as ran

def customerLoop(customer,recipe):
    if ran.randint(0,1) == 0:
        purchase = 1
    else:
        purchase = 0
    return purchase