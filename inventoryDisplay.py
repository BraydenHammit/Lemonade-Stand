def displayInv(inventory,recipe,cupsMade,profits,cupsBought,moneySpent,endOfDay,taxes):
    print('Money:',inventory["money"])
    print('Ice:',inventory["ice"])
    print('Lemons:',inventory["lemons"])         #print inventory
    print('Sugar:',inventory["sugar"])
    print('Water:',inventory["water"])
    print('Cups:',inventory["cups"])
    if endOfDay:                # only print this if it's the end of day report
        print(f'Recipe:\n  Lemons - {recipe["lemons"]}\n  Ice - {recipe["ice"]}\n  Sugar - {recipe["sugar"]}\n  Water - {recipe["water"]}\n  Cost - {recipe["cost"]}')
        print('Cups made:',cupsMade)
        print('Customer purchases:',cupsBought)
        print('Money earned:',profits)
        print('You spent:',moneySpent)
        if taxes == 0:
            print('Daily taxes...?')        # if you evaded
        else:
            print('Daily taxes:',taxes)
        print('Total profit:',round(profits-moneySpent-taxes,2))
        if inventory["permit"] == 0:
            print("Your permit is expired!")
        elif inventory["permit"] == 1:
            print('Your permit expires tommorow!')
        else:
            print(f'Permit exipiration: {int(inventory["permit"])} days')