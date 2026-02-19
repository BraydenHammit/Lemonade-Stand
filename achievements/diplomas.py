import tkinter as tk

def diplomaM():
    diploma30 = tk.Tk()
    diploma30.title("1 Month of Lemonade Stand")
    diploma30.geometry('1512x2016') #replace with photo size
    image30 = tk.PhotoImage(file='diploma30.png')
    label30 = tk.Label(diploma30, image=image30)
    label30.place(x=0, y=0, relwidth=1, relheight=1)

    diploma30.mainloop()



def diplomaY():
    diploma365 = tk.Tk()
    diploma365.title("1 Year of Lemonade Stand")
    diploma365.geometry('100x100') #replace with photo size
    image30 = tk.PhotoImage(file='diploma365.png')
    label30 = tk.Label(diploma365, image=image30)
    label30.place(x=0, y=0, relwidth=1, relheight=1)

    diploma365.mainloop()
