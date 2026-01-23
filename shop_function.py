def purchasing(money,ingredients):
    purchaseType = input('What would you like to buy? (i/l/s) ')
    purchaseAmount = int(input('How many would you like to buy? '))

    if purchaseType == 'i':
        if money - 2.5*purchaseAmount > 0:
            money -= 2.5*purchaseAmount
            ingredients[0] += purchaseAmount

    elif purchaseType == 'l':
        if money - 4*purchaseAmount > 0:
            money -= 4*purchaseAmount
            ingredients[1] += purchaseAmount

    elif purchaseType == 's':
        if money - 3*purchaseAmount > 0:
            money -= 3*purchaseAmount
            ingredients[2] += purchaseAmount
            
    return [money,ingredients]
