import random as ran

def customerLoop(customer,recipe):
    pref = customer.get_customer_attributes()
    sweetness = recipe["sugar"] - recipe["lemons"]
    purchase = 0
    reason = []

    if customer["duck"]:
        purchase = False
        reason.append('No Grapes')

    else:
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

        if (pref["leniency"] >= 0 and pref["water"] - recipe["water"] >= 0) or (pref["leniency"] <= 0 and pref["water"] - recipe["water"] <= 0):
            purchase += 1
        else:
            if pref["leniency"] >= 0:                  
                reason.append('Too Diluted')
            else:
                reason.append('Too Concentrated')


        if pref["price"] >= recipe["cost"]:
            purchase += 1
        else:
            reason.append('Too Expensive')

        if purchase == 4 or (purchase == 3 and ran.randint(0,1) == 1) or (purchase == 2 and ran.randint(1,3) == 3):          #if they dont't have a problem, if they only have one it's a 50% chance, if they have two its a 33% chance
            purchase = True
        else: 
            purchase = False

    return purchase, reason