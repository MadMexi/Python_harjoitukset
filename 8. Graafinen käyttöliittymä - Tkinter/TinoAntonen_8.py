import tkinter as tk

#nappiin kytketty toiminto
# parametri1 = input()
# parametri2 = input()
def plus(parametri1,parametri2):
    print(parametri1 + parametri2)
def miinus():
    print("")
def kerto():
    print("")
def jako():
    print("")
    
#Tkinter-ikkunan luonti
ikkuna = tk.Tk()    
ikkuna.title("Laskin")
ikkuna.geometry("400x300")
    
#nappeja eri parametreillä    
nappi1 = tk.Button(ikkuna, text="+", command=plus)
nappi1.place(x = 120, y = 100)

nappi2 = tk.Button(ikkuna, text="-", command=miinus)
nappi2.place(x = 170, y = 100)

nappi3 = tk.Button(ikkuna, text="*", command=kerto)
nappi3.place(x = 220, y = 100)

nappi4 = tk.Button(ikkuna, text="/", command=jako)
nappi4.place(x = 270, y = 100)

nappi5 = tk.Button(ikkuna, text="1", command=jako)
nappi5.place(x = 160, y = 160)

nappi6 = tk.Button(ikkuna, text="2", command=jako)
nappi6.place(x = 190, y = 160)

nappi7 = tk.Button(ikkuna, text="3", command=jako)
nappi7.place(x = 220, y = 160)

nappi8 = tk.Button(ikkuna, text="4", command=jako)
nappi8.place(x = 160, y = 190)

nappi9 = tk.Button(ikkuna, text="5", command=jako)
nappi9.place(x = 190, y = 190)

nappi10 = tk.Button(ikkuna, text="6", command=jako)
nappi10.place(x = 220, y = 190)

nappi11 = tk.Button(ikkuna, text="7", command=jako)
nappi11.place(x = 160, y = 220)

nappi12 = tk.Button(ikkuna, text="8", command=jako)
nappi12.place(x = 190, y = 220)

nappi13 = tk.Button(ikkuna, text="9", command=jako)
nappi13.place(x = 220, y = 220)

nappi14 = tk.Button(ikkuna, text="0", command=jako)
nappi14.place(x = 190, y = 250)

nappi15 = tk.Button(ikkuna, text="=", command=jako)
nappi15.place(x = 190, y = 130)

#käynnistä ikkuna
ikkuna.mainloop()
