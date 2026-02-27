import tkinter as tk

def achievementM():
    achievement30 = tk.Tk()
    achievement30.title("1 Month of Lemonade Stand")
    achievement30.geometry('216x288') #replace with photo size
    image30 = tk.PhotoImage(file='achievements/achievement30.png')
    label30 = tk.Label(achievement30, image=image30)
    label30.place(x=0, y=0, relwidth=1, relheight=1)

    achievement30.mainloop()



def achievementY():
    achievement365 = tk.Tk()
    achievement365.title("1 Year of Lemonade Stand")
    achievement365.geometry('216x288') #replace with photo size
    image30 = tk.PhotoImage(file='achievements/achievement365.png')
    label30 = tk.Label(achievement365, image=image30)
    label30.place(x=0, y=0, relwidth=1, relheight=1)

    achievement365.mainloop()


def achievementX():
    achievement50K = tk.Tk()
    achievement50K.title("1 Year of Lemonade Stand")
    achievement50K.geometry('216x288') #replace with photo size
    image30 = tk.PhotoImage(file='achievements/achievement50K.png')
    label30 = tk.Label(achievement50K, image=image30)
    label30.place(x=0, y=0, relwidth=1, relheight=1)

    achievement50K.mainloop()
