def displayInv(inventory,recipe,cupsMade,profits,cupsBought,moneySpent,endOfDay,taxes):
    print('Money:',inventory["money"])
    print('Ice:',inventory["ice"])
    print('Lemons:',inventory["lemons"])         #print inventory
    print('Sugar:',inventory["sugar"])
    print('Cups:',inventory["cups"])
    if endOfDay:
        print(f'Recipe:\n  Lemons - {recipe["lemons"]}\n  Ice - {recipe["ice"]}\n  Sugar - {recipe["sugar"]}\n  Cost - {recipe["cost"]}')
        print('Cups made:',cupsMade)
        print('Money earned:',profits)
        print('Customer purchases:',cupsBought)
        print('You spent:',moneySpent)
        print('Daily taxes:',taxes)
        print('Total profit:',profits-moneySpent-taxes)