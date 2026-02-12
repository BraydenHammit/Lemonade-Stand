def displayInv(inventory,recipe,cupsMade,profits,cupsBought,endOfDay):
    print('Money:',inventory["money"])
    print('Ice:',inventory["ice"])
    print('Lemons:',inventory["lemons"])         #print inventory
    print('Sugar:',inventory["sugar"])
    print('Cups:',inventory["cups"])
    if endOfDay:
        print('Recipe:',recipe)
        print('Cups made:',cupsMade)
        print('Money earned:',profits)
        print('Purchases:',cupsBought)