def purchasing(inventory):
    purchaseType = 'n/a'

    while purchaseType != 'done':
        purchaseType = input('What would you like to buy? Ice, lemons, sugar, or cups? (i/l/s/c/done) ')

        if purchaseType != 'done':
                try:
                    purchaseAmount = int(input('How many would you like to buy? '))
                    break
                except ValueError:    
                    print("Not an integer Value")

        if purchaseType == 'i':
            if inventory["money"] - .75*purchaseAmount > 0:
                inventory["money"] -= .75*purchaseAmount
                inventory["ice"] += purchaseAmount
            else:
                print('Too expensive!')

        elif purchaseType == 'l':
            if inventory["money"] - 1*purchaseAmount > 0:
                inventory["money"] -= 1*purchaseAmount
                inventory["lemons"] += purchaseAmount
            else:
                print('Too expensive!')

        elif purchaseType == 's':
            if inventory["money"] - .5*purchaseAmount > 0:
                inventory["money"] -= .5*purchaseAmount
                inventory["sugar"] += purchaseAmount
            else:
                print('Too expensive!')

        elif purchaseType == 'c':
            if inventory["money"] - .25*purchaseAmount > 0:
                inventory["money"] -= .25*purchaseAmount
                inventory["cups"] += purchaseAmount
            else:
                print('Too expensive!')
        
        elif purchaseType != 'done':
            print('Invalid item!')
                
    return inventory
