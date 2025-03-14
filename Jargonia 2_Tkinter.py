import tkinter as tk
#nappiin kytketty toiminto
def toiminto():
    print("Miisu")
def toiminto2():
    print("koira")
#Tkinter-ikkunan luonti
ikkuna = tk.Tk()    
ikkuna.title("kissa")
ikkuna.geometry("300x200")
    
#nappeja eri parametreillä    
nappi1 = tk.Button(ikkuna, text="Nappi 1", command=toiminto)
nappi1.place(x = 90, y = 100)

nappi2 = tk.Button(ikkuna, text="Nappi 2", command=toiminto2)
nappi2.place(x = 160, y = 100)
#käynnistä ikkuna
ikkuna.mainloop()
    
    
    
    
    
    