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
      if ran.randint(1,3) != 3:       # 33% chance to succeed in evading
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




def loopYN(type):   # used whenever an option is needed (shop open / recipe change)
  yn = 'n/a'
  while yn != 'n' and yn != 'N' and yn != 'y' and yn != 'Y':
    if type == 'r':
      yn = input('Would you like to edit your recipe? (y/n) ')
    elif type == 's':
      yn = input('Would you like to open the shop? (y/n) ')
    if yn != 'n' and yn != 'N' and yn != 'y' and yn != 'Y':
      print('Invalid answer!')
  if yn == 'y' or yn == 'Y':
    return True
  else:
    return False