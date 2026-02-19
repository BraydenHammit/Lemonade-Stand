def customerLoop(customer,recipe):
    pref = customer.get_customer_attributes(customer)
    sweetness = recipe["sugar"] - (recipe["lemons"]//2)
    purchase = 0
    reason = None

    if (pref["leniency"] >= 0 and pref["sweetness"] - sweetness >= 0) or (pref["leniency"] <= 0 and pref["sweetness"] - sweetness <= 0):
        purchase += 1
    else:
        if pref["leniency"] >= 0:                
            reason = 'Too Sweet'
        else:
            reason = 'Too Sour'
    
    if (pref["leniency"] >= 0 and pref["ice"] - recipe["ice"] >= 0) or (pref["leniency"] <= 0 and pref["ice"] - recipe["ice"] <= 0):
        purchase += 1
    else:
        if pref["leniency"] >= 0:                  
            reason = 'Too Cold'
        else:
            reason = 'Too Warm'


    if pref["price"] >= recipe["price"]:
        purchase += 1
    else:
        reason = 'Too Expensive'

    if purchase >= 2:
        purchase = True
    else: 
        purchase = False

    return purchase, reason