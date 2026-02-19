import random as ran

def customerLoop(customer,recipe):
    customer.__init__(customer, sweetness_preference=None, ice_preference=None, price_point=None, leniency=None)
    pref = customer.get_customer_attributes(customer)
    sweetness = recipe["sugar"] - recipe["lemons"]
    purchase = 0
    reason = []

    if (pref["leniency"] >= 0 and pref["sweetness"] - sweetness >= 0) or (pref["leniency"] <= 0 and pref["sweetness"] - sweetness <= 0):
        purchase += 1
    else:
        if pref["leniency"] >= 0:                
            reason.append('Too Sweet')
        else:
            reason.append('Too Sour')
    
    if (pref["leniency"] >= 0 and pref["ice"] - recipe["ice"] >= 0) or (pref["leniency"] <= 0 and pref["ice"] - recipe["ice"] <= 0):
        purchase += 1
    else:
        if pref["leniency"] >= 0:                  
            reason.append('Too Cold')
        else:
            reason.append('Too Warm')


    if pref["price"] >= recipe["cost"]:
        purchase += 1
    else:
        reason.append('Too Expensive')

    if purchase == 3 or (purchase == 2 and ran.randint(0,1) == 1):
        purchase = True
    else: 
        purchase = False

    return purchase, reason