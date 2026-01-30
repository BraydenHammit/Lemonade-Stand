def maxCupCalculate(recipe,inventory):
    maxCups = (recipe['lemons'] * inventory['lemons'])+(recipe['ice'] * inventory['ice'])+(recipe['sugar'] * inventory['sugar'])