from Tkinter import * 
import time

# Create objects
w = Tk(); f = Frame(); f.pack()
time_var = StringVar()
time_labelis = Label(f, textvariable=time_var, font="Courier 60", bg="Black", fg="#00B000")
time_labelis.pack()

# Create function for flashing
def mirgot():
    """Funkcija datu atjaunoshanai""" 
    t = time.localtime(time.time())
    if t[5] % 2:                        # mirgoshanas efekts fmt = "%H:%M"
        fmt = "%H %M"
    else:
        time_var.set(time.strftime(fmt, t)) 
        time_labelis.after(500, mirgot) # gaidam 0.5sec
        
time_labelis.after(500, mirgot) 
w.mainloop()
