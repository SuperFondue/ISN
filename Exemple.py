#~import bibli
from tkinter import *
from random import *

#fonctions
def chgClr():
        global couleur
        if randint(0, 1)==1:
            lbl1.configure(bg=couleur2)
            couleur=couleur2
            bt1.configure(text="Pile", fg="brown")
        else:
            lbl1.configure(bg=couleur1)
            couleur=couleur1
            bt1.configure(text="Face", fg="pink")

def reset():
        global couleur
        global info
        couleur="#FFFFFF"
        lbl1.configure(bg=couleur)
        bt1.configure(text=info)

#variables       
couleur1="#D2691E"
couleur2="#FF1493"
couleur="#FFFFFF"
info="Clique ici !"
r="Remise à zéro"

#Prg Ppal

fen=Tk()

bt1=Button(fen,width=20,text=info,cursor="hand2",command=chgClr)
bt1.grid(row=2,column=0)

bt2=Button(fen,width=20,text=r,cursor="hand2",command=reset)
bt2.grid(row=3,column=0)

lbl1=Label(fen,bg=couleur,width=20)
lbl1.grid(row=1,column=0)

fen.mainloop()
