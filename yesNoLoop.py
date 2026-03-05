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




def loopYN(type):   # used whenever an option is needed (shop open / recipe change / bet)
  yn = 'n/a'
  repeats = 0
  while ((yn != 'n' and yn != 'N' and type != 'b') and yn != 'y' and yn != 'Y') or (yn != 'y' and yn != 'Y' and type == 'b'):
    if yn.lower() == 'n':
      if repeats == 0:
        print('Are you sure?')
      elif repeats == 1:
        print('You should reconsider.')
      elif repeats == 2:
        print('Remember, this game is called Lemonade Stand.')
      else:
        print('Accept the bet.')
      repeats += 1

    if type == 'r':
      yn = input('Would you like to edit your recipe? (y/n) ')

    elif type == 's':
      yn = input('Would you like to open the shop? (y/n) ')

    elif type == 'b':
      yn = input('Do you accept the bet? (y/n) ')

    elif type == 'st':
      yn = input('Do you want to hear the backstory? (y/n) ')

    elif type == 'w':
      yn = input('Do you want to keep going and try to get to 50K? (y/n) ')

    elif type == '50':
      yn = input('Do you want to continue to endless mode? (y/n) ')


    if yn != 'n' and yn != 'N' and yn != 'y' and yn != 'Y':
      print('Invalid answer!')



  if yn == 'y' or yn == 'Y':
    return True
  else:
    return False