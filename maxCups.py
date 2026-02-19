def maxCupCalculate(recipe,inventory):
    maxCupsL = (inventory['lemons']//recipe['lemons'])

    maxCupsW = (inventory['water']//recipe['water'])

    if recipe['ice'] != 0:
        maxCupsI = (inventory['ice']//recipe['ice'])
    else:
        maxCupsI = 999999

    if recipe['sugar'] != 0:
        maxCupsS = (inventory['sugar']//recipe['sugar'])
    else:
        maxCupsS = 999999

    return min(maxCupsL,maxCupsI,maxCupsW,maxCupsS,inventory["cups"])            #the minimum value is the restricting value, therefore it's the max amount