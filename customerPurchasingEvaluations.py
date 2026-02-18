import random as ran

def customerLoop(customer,recipe):
    pref = customer.get_customer_attributes(customer)
    sweetness = recipe["sugar"] - (recipe["lemons"]//2)

    if (pref["leniency"] >= 0 and pref["sweetness"] - sweetness >= 0) or (pref["leniency"] <= 0 and pref["sweetness"] - sweetness <= 0):
        reason = None
    else:
        purchase = 0
        if pref["leniency"] >= 0:                   #debug this and make sure it works
            reason = 'Too Sweet'
        else:
            reason = 'Too Sour'

    if ran.randint(0,1) == 0:
        purchase = 1
    else:
        purchase = 0

    return purchase, reason