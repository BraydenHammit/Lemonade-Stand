def maxCupCalculate(recipe,inventory):
    maxCupsL = (inventory['lemons']//recipe['lemons'])

    if recipe['ice'] != 0:
        maxCupsI = (inventory['ice']//recipe['ice'])
    else:
        maxCupsI = 999999

    if recipe['sugar'] != 0:
        maxCupsC = (inventory['sugar']//recipe['sugar'])
    else:
        maxCupsC = 999999

    return min(maxCupsL,maxCupsI,maxCupsC,inventory["cups"])            #the minimum value is the restricting value, therefore it's the max amount