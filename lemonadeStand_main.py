import shop_function as shopF
import tkinter as tk
import random as ran

root = tk.Tk()
root.title('Lemonade Stand')                  #screen / ui
root.geometry('700x500')

money = 100
ice = 0
lemons = 0
sugar = 0

while money > 0:
    list = shopF.purchasing(money,[ice,lemons,sugar])   #daily purchasing

    money = list[0]
    ice = list[1][0]
    lemons = list[1][1]
    sugar = list[1][2]

    money += ran.randint(0,5)   #replace when we code customers

    print('Money:',money)
    print('Ice:',ice)
    print('Lemons:',lemons)         #print inventory
    print('Sugar:',sugar)