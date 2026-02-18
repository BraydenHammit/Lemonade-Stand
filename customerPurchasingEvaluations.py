import random as ran

def customerLoop(customer,recipe):
    pref = customer.get_customer_attributes(customer)
    sweetness = recipe["sugar"] - (recipe["lemons"]//2)

    if (pref["leniency"] >= 0 and pref["sweetness"] - sweetness >= 0) or (pref["leniency"] <= 0 and pref["sweetness"] - sweetness <= 0):
        reason = None
    else:
        purchase = 0
        if pref["leniency"] >= 0:                
            reason = 'Too Sweet'
        else:
            reason = 'Too Sour'
    
    if (pref["leniency"] >= 0 and pref["ice"] - recipe["ice"] >= 0) or (pref["leniency"] <= 0 and pref["ice"] - recipe["ice"] <= 0):
        reason = None
    else:
        purchase = 0
        if pref["leniency"] >= 0:                  
            reason = 'Too Cold'
        else:
            reason = 'Too Warm'


            #add cost pref

    return purchase, reason