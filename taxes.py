import time as t
import random as ran

def taxes(inventory, tax):
    evade = 'n/a'
    print("========================================== TAXES ==========================================")       
    while evade != 'n' and evade != 'N' and evade != 'y' and evade != 'Y':
      evade = input(f'Would you like to attempt to evade your taxes of {tax}? (y/n) ')
      if evade != 'n' and evade != 'N' and evade != 'y' and evade != 'Y':           #tax evasion decision code
        print('Invalid answer!')
    if evade == 'Y' or evade == 'y':
      if ran.randint(1,3) == 3:       # 33% chance to succeed in evading
        print('You...succeeded. ')
        t.sleep(3)
        print("Don't do it again.")
        t.sleep(3)
        tax = 0
      else:
        inventory = 'death'
    else:
      inventory["money"] -= tax          #apply tax if not evaded

    return inventory, tax