from interfazGR import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class help:
    def __init__(self):
        self.hlg = Tk()
        self.hlg.resizable(True,False) # Redimensionar la ventana
        self.hlg.title('..::ADF::..') # Titulo de la ventana
        self.hlg.geometry('1000x700') # Tamaño de la ventana
        self.Centrarhlg(self.hlg, 1000, 700) # Centrar la ventana
        self.hlg.config(bg='#102027')
        self.Ventanahlg() # Llamar a la ventana

    def Centrarhlg(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight() # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth() # Ancho de la pantalla

        print("Altura de la pantalla: ", altura_pantalla)
        print("Ancho de la pantalla: ", ancho_pantalla)

        x = (ancho_pantalla // 2) - (ancho // 2) # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2) # Posicion de la ventana
        r.geometry(f'+{x}+{y}') # Posicion de la ventana

    def Ventanahlg(self):
        Label(self.hlg, text="...:::...Creación de Automatas...:::...", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=200, y=20)
        Label(self.hlg, text="Ingrese el nombre del automata:", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=50)
        Label(self.hlg, text="Ingrese los estados del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=80)
        Label(self.hlg, text="Ingrese el alfabeto del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=110)
        Label(self.hlg, text="Ingrese el estado inicial del automata: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=140)
        Label(self.hlg, text="Ingrese los estados de aceptacion del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=170)
        Label(self.hlg, text="Ingrese las transiciones del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=200)

        self.hlg.mainloop()